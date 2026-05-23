import pandas as pd
import numpy as np
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'data.csv')

COLUMN_MAP = {
    'User ID': 'user_id',
    'Record Date': 'record_date',
    'Age': 'age',
    'Gender': 'gender',
    'Occupation': 'occupation',
    'Education Level': 'education_level',
    'Social Media Time hrs': 'social_media_time',
    'Gaming Time hrs': 'gaming_time',
    'Streaming Time hrs': 'streaming_time',
    'Work Study Time hrs': 'work_study_time',
    'Browsing Time hrs': 'browsing_time',
    'Total Screen Time hrs': 'total_screen_time',
    'Daily App Opens': 'daily_app_opens',
    'Avg Session Duration min': 'avg_session_duration',
    'Nighttime Usage hrs': 'nighttime_usage',
    'Notifications per Day': 'notifications_per_day',
    'Phone Pickups per Hour': 'phone_pickups_per_hour',
    'Binge Sessions per Week': 'binge_sessions_per_week',
    'FOMO Score 1 10': 'fomo_score',
    'Anxiety Without Phone 1 10': 'anxiety_score',
    'Sleep Disruption Score 1 10': 'sleep_disruption_score',
    'Mood After Usage': 'mood_after_usage',
    'Attempted Reduction': 'attempted_reduction',
    'Reduction Success': 'reduction_success',
    'Social Interaction Impact': 'social_interaction_impact',
    'Physical Activity hrs': 'physical_activity',
    'Sleep Hours': 'sleep_hours',
    'Productivity Score 1 10': 'productivity_score',
    'Most Used Platform': 'most_used_platform',
    'Second Most Used Platform': 'second_most_used_platform',
    'Addiction Risk Score': 'addiction_risk_score',
    'Risk Category': 'risk_category',
    'Addiction Label': 'addiction_label',
}

def find_header_row(file_path_or_buf):
    if hasattr(file_path_or_buf, 'seek'):
        file_path_or_buf.seek(0)
    try:
        temp_df = pd.read_csv(file_path_or_buf, header=None, nrows=10, dtype=str)
        if hasattr(file_path_or_buf, 'seek'):
            file_path_or_buf.seek(0)
    except Exception:
        if hasattr(file_path_or_buf, 'seek'):
            file_path_or_buf.seek(0)
        return 0
    
    best_row_idx = 0
    max_matches = 0
    for idx, row in temp_df.iterrows():
        row_vals = [str(val).strip() for val in row.dropna()]
        matches = sum(1 for val in row_vals if val in COLUMN_MAP)
        if matches > max_matches:
            max_matches = matches
            best_row_idx = idx
            
    if max_matches >= 2:
        return best_row_idx
    return 0

def load_data(uploaded_file=None):
    try:
        if uploaded_file is not None:
            header_idx = find_header_row(uploaded_file)
            if hasattr(uploaded_file, 'seek'):
                uploaded_file.seek(0)
            raw = pd.read_csv(uploaded_file, skiprows=header_idx, header=0, low_memory=False)
        else:
            header_idx = find_header_row(DATASET_PATH)
            raw = pd.read_csv(DATASET_PATH, skiprows=header_idx, header=0, low_memory=False)

        raw.columns = raw.columns.str.strip()
        rename = {k: v for k, v in COLUMN_MAP.items() if k in raw.columns}
        df = raw.rename(columns=rename)

        # Parse date
        if 'record_date' in df.columns:
            df['record_date'] = pd.to_datetime(df['record_date'], errors='coerce', format='mixed')
            df['month'] = df['record_date'].dt.month.astype('Int64')
            df['day_of_week'] = df['record_date'].dt.day_name()
            df['week'] = df['record_date'].dt.isocalendar().week.astype('Int64')

        # Numeric coerce
        num_cols = ['age', 'social_media_time', 'gaming_time', 'streaming_time',
                    'work_study_time', 'browsing_time', 'total_screen_time',
                    'daily_app_opens', 'avg_session_duration', 'nighttime_usage',
                    'notifications_per_day', 'phone_pickups_per_hour',
                    'binge_sessions_per_week', 'fomo_score', 'anxiety_score',
                    'sleep_disruption_score', 'physical_activity', 'sleep_hours',
                    'productivity_score', 'addiction_risk_score', 'addiction_label']
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Robust check for core columns
        core_cols = ['total_screen_time', 'addiction_risk_score']
        existing_core = [c for c in core_cols if c in df.columns]
        
        if len(existing_core) < len(core_cols):
            missing = set(core_cols) - set(existing_core)
            # If columns are missing, we don't dropna on them, but we notify or handle it
            pass 

        if 'total_screen_time' in df.columns:
            df = df.dropna(subset=['total_screen_time'])
            
        df = df.reset_index(drop=True)
        return df
    except Exception as e:
        raise RuntimeError(f"Data load error: {e}")

def get_summary_stats(df):
    return {
        'total_records': len(df),
        'avg_screen_time': round(df['total_screen_time'].mean(), 2) if 'total_screen_time' in df.columns else 0.0,
        'avg_risk_score': round(df['addiction_risk_score'].mean(), 2) if 'addiction_risk_score' in df.columns else 0.0,
        'high_risk_pct': round((df['risk_category'].str.lower().isin(['high', 'critical'])).mean() * 100, 1) if 'risk_category' in df.columns else 0.0,
        'avg_sleep': round(df['sleep_hours'].mean(), 2) if 'sleep_hours' in df.columns else 0.0,
        'avg_notifications': round(df['notifications_per_day'].mean(), 1) if 'notifications_per_day' in df.columns else 0.0,
        'avg_night_usage': round(df['nighttime_usage'].mean(), 2) if 'nighttime_usage' in df.columns else 0.0,
        'binge_avg': round(df['binge_sessions_per_week'].mean(), 1) if 'binge_sessions_per_week' in df.columns else 0.0,
    }
