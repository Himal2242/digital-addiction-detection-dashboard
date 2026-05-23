<div align="center">

<h1>🧠 AdaptiveAI — Digital Addiction Detection Dashboard</h1>

<p>
  <b>An Enterprise-Level Adaptive Intelligence System for detecting, analyzing, and managing digital addiction patterns using Machine Learning, Behavioral Analytics, and Real-Time Data Visualization.</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Dataset-20%2C000%20Records-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ML%20Models-3%20Algorithms-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Anomaly%20Detection-Isolation%20Forest-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Mobile-ADB%20Integration-lightgrey?style=for-the-badge" />
</p>

</div>

---

## 📸 Screenshots

| Overview Dashboard | Advanced Dashboard |
|---|---|
| ![Overview](Screenshots/Screenshot%202026-05-24%20001531.png) | ![Advanced](Screenshots/Screenshot%202026-05-24%20001625.png) |

| Session Burst Analysis | Risk Hierarchy Sunburst |
|---|---|
| ![Sessions](Screenshots/Screenshot%202026-05-24%20001554.png) | ![Sunburst](Screenshots/Screenshot%202026-05-24%20001729.png) |

---

## 🌟 What is AdaptiveAI?

**AdaptiveAI** is a full-stack data intelligence platform built with **Python + Streamlit** that helps individuals, parents, and organizations understand and combat **digital addiction** through:

- 📊 **Rich, Interactive Dashboards** — KPIs, charts, heatmaps, and sunburst visualizations
- 🤖 **3 Machine Learning Models** — Logistic Regression, Linear/Multiple Regression, and Random Forest
- 🧠 **Behavior Intelligence Engine** — Focus scores, distraction index, FOMO, dopamine loop detection
- ⚡ **Custom Risk Scoring Engine** — Weighted formula-based real-time risk gauge
- 💡 **AI Recommendation System** — Personalized 7-day digital detox plan
- 📱 **Android ADB Integration** — Pull live usage data from real devices
- 🔐 **Role-Based Authentication** — User, Parent, and Admin access tiers

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Himal2242/digital-addiction-detection-dashboard.git
cd digital-addiction-detection-dashboard
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your settings if needed
```

### 5. Launch the App
```bash
streamlit run app.py
```

### 6. Open in Browser
```
http://localhost:8501
```

---

## 🔐 Demo Login Credentials

| Role   | Username | Password       | Access                        |
|--------|----------|----------------|-------------------------------|
| Admin  | `admin`  | `admin123`     | Full access + Admin Panel     |
| Parent | `parent` | `parent123`    | Dashboard + Monitoring        |
| User   | Sign up  | Any (≥6 chars) | Personal analytics + Reports  |

---

## 📁 Project Structure

```
digital-addiction-detection-dashboard/
│
├── app.py                        # 🏠 Main Streamlit application (1500+ lines)
├── requirements.txt              # 📦 Python dependencies
├── .env.example                  # 🔑 Environment variable template
├── data.csv                      # 📊 Primary dataset (20,000 records)
│
├── auth/
│   ├── __init__.py
│   └── auth.py                   # 🔐 Login, Signup, Sessions, SQLite auth
│
├── data/
│   ├── __init__.py
│   └── users.db                  # 🗄️ Auto-created SQLite user database
│
├── dataset/
│   ├── __init__.py
│   └── sample_data.csv           # 📁 Sample dataset
│
├── ml_models/
│   ├── __init__.py
│   └── models.py                 # 🤖 LogReg, Linear Regression, Random Forest
│
├── behavior_analysis/
│   ├── __init__.py
│   └── analyzer.py               # 🧠 Behavioral metrics & anomaly detection
│
├── integrations/
│   ├── __init__.py
│   └── adb_integration.py        # 📱 Android ADB + simulation module
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py            # 📂 CSV parsing + feature engineering
│   ├── recommendations.py        # 💡 Personalized recommendation engine
│   └── ocr_utils.py              # 🔍 OCR image data extraction
│
└── Screenshots/                  # 🖼️ Application screenshots
```

---

## ✨ Features In Depth

### 🔐 1. Authentication System
- Secure Signup / Login / Logout flow
- **SHA-256** password hashing
- **Role-based access control**: User → Parent → Admin
- Persistent **SQLite** database (auto-created on first run)

---

### 📊 2. Overview Dashboard
Real-time KPI cards and visualizations across your 20,000-record dataset:
- 📌 **KPI Cards**: Total Records, Avg Screen Time, Risk Score, High Risk %, Sleep, Notifications
- 🥧 **Risk Category Pie Chart** — Low / Moderate / High / Critical breakdown
- 📊 **Top 10 Most Used Platforms** — Horizontal bar chart
- 📈 **Screen Time Histogram** — Distribution analysis
- 🎯 **Session Burst Scatter Plot** — Bubble chart with notification density

---

### 📈 3. Advanced Dashboard
Drill-down analytics with **multi-dimensional filters** (Risk, Occupation, Gender):
- 📉 **Monthly Screen Time Trend** — Line chart
- 🌓 **Day vs Night Usage Comparison** — Grouped bar chart
- 🔥 **Notification Heatmap** — Risk Category × Day of Week
- 🌞 **Risk Hierarchy Sunburst** — Risk → Occupation → Platform
- 📊 **Feature Correlation Matrix** — 10-feature heatmap
- 💤 **Sleep vs Productivity Scatter** — Insight into health impact

---

### 🧠 4. Behavior Intelligence Module
Advanced behavioral analytics and anomaly detection:

| Metric | Description |
|--------|-------------|
| **Focus Score** | Inverse of distraction indicators |
| **Distraction Index** | Phone pickups, notifications, binge sessions |
| **Digital Dependency Score** | Composite addiction indicator |
| **Dopamine Loop %** | % of users in compulsive usage cycles |
| **FOMO-Driven %** | Users with high FOMO anxiety correlation |
| **Night Dominant %** | Heavy late-night screen usage |

**Anomaly Detection:**
- 🔬 **Isolation Forest** — Unsupervised outlier detection
- 📐 **Z-Score Method** — Statistical extreme value detection (z > 3)
- Auto-generated plain-English behavioral insights

---

### 🤖 5. Machine Learning Predictions

#### Tab 1 — Addiction Risk (Logistic Regression)
- Binary classification: **Addicted vs Not Addicted**
- Confusion Matrix, Accuracy, Precision, Recall
- Feature Importance (|Coefficients|)
- **Live Prediction Form** — Enter your own values, get instant results with explanations

#### Tab 2 — Screen Time Forecast (Linear & Multiple Regression)
- Predict daily screen time from behavioral features
- Actual vs Predicted comparison chart
- **MAE**, **RMSE** error metrics
- Residuals distribution histogram

#### Tab 3 — Behavior Pattern (Random Forest)
- Multi-class classification: **Productive / Neutral / Addictive**
- 100 decision trees, feature importance ranking
- Prediction confidence bar chart (first 50 samples)
- Full confusion matrix

---

### ⚡ 6. Risk Scoring Engine
Custom-weighted addiction risk formula:

```
Risk Score = (Screen Time × 40%) + (Night Usage × 20%) + (Notifications × 20%) + (Sessions × 20%)
```

- 🎯 **Plotly Gauge Chart** — Visual risk meter (0–100)
- 📊 **Score Breakdown Bar** — Per-component contribution
- 📈 **Population Distribution** — Compare your score vs entire dataset

---

### 💡 7. Recommendation Engine
Personalized AI-generated recovery plans:
- 🚨 **Critical Alerts** for high-risk users
- ⚠️ **Warnings** for moderate behavior
- 📋 **7-Day Wellness Plan** with daily goals
- 🧘 **Digital Detox Plan** — App blocking, notification management, sleep hygiene

---

### 👨‍💼 8. Admin Panel *(Admin role only)*
- View all registered users and roles
- Dataset statistics and health checks

---

### ⚙️ 9. Settings / Profile
- Profile viewer with account details
- **CSV Upload** — Use your own custom dataset
- **ADB Device Connection** — Real Android device data integration
- **Simulation Mode** — Generate 200 realistic synthetic mobile records
- **OCR Upload** — Extract data from screenshots of usage stats

---

## 📱 Mobile Integration (ADB)

### Real Device Mode
Connect your Android phone and pull live usage statistics:
```bash
# Enable USB Debugging on your Android device, then:
adb devices
# The app will auto-detect and fetch real data
```

### Simulation Mode
No device? No problem.
- Navigate to **Settings → Mobile Integration**
- Click **"Generate Simulated Mobile Data"**
- Instantly generates 200 realistic app-usage records

---

## 🧪 Dataset Schema

The dataset must contain these columns (supports custom CSV uploads):

| Category | Columns |
|----------|---------|
| **Demographics** | Age, Gender, Occupation, Education Level |
| **Screen Time** | Social Media, Gaming, Streaming, Work/Study, Browsing, Total |
| **Behavioral** | Daily App Opens, Avg Session Duration, Nighttime Usage |
| **Psychological** | FOMO Score, Anxiety Score, Sleep Disruption Score |
| **Health Impact** | Productivity Score, Sleep Hours, Physical Activity |
| **Labels** | Addiction Risk Score, Risk Category, Addiction Label |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **UI Framework** | Streamlit ≥ 1.32 |
| **Visualizations** | Plotly ≥ 5.18 |
| **Machine Learning** | Scikit-learn ≥ 1.3 |
| **Data Processing** | Pandas ≥ 2.0, NumPy ≥ 1.24 |
| **Statistics** | SciPy ≥ 1.11 |
| **Authentication** | SQLite + SHA-256 |
| **Navigation** | streamlit-option-menu |
| **Mobile Data** | Android Debug Bridge (ADB) |
| **OCR** | Tesseract + Pillow |

---

## ⚙️ System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Python** | 3.8+ | 3.10+ |
| **RAM** | 4 GB | 8 GB |
| **Storage** | 500 MB | 1 GB |
| **OS** | Windows / macOS / Linux | Any |

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ Module Not Found Errors</b></summary>

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```
</details>

<details>
<summary><b>📱 ADB Connection Issues</b></summary>

1. Enable **USB Debugging** in Android Developer Options
2. Install [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools)
3. Run `adb devices` — your device should appear
4. Accept the RSA fingerprint prompt on your device
</details>

<details>
<summary><b>🗄️ Database / SQLite Issues</b></summary>

The SQLite database is auto-created on first run. If issues occur:
```bash
# Ensure data/ directory is writable
mkdir data
# Delete and recreate the DB
del data\users.db
streamlit run app.py
```
</details>

<details>
<summary><b>🔌 Port Already in Use</b></summary>

```bash
streamlit run app.py --server.port 8502
```
</details>

<details>
<summary><b>🔍 Tesseract / OCR Not Working</b></summary>

The app will auto-install `pytesseract` and `Pillow` on first launch. If it fails:
```bash
pip install pytesseract Pillow
# Also install Tesseract OCR engine from: https://github.com/UB-Mannheim/tesseract/wiki
```
</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/YourAmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add: YourAmazingFeature"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/YourAmazingFeature
   ```
5. **Open a Pull Request** — describe what you added and why

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 📞 Support

- 🐛 **Found a bug?** [Open an Issue](https://github.com/Himal2242/digital-addiction-detection-dashboard/issues)
- 💬 **Have a question?** Start a [Discussion](https://github.com/Himal2242/digital-addiction-detection-dashboard/discussions)
- ⭐ **Like the project?** Give it a star — it means a lot!

---

<div align="center">

Made with ❤️ and Python

⭐ Star this repo if you found it useful!

</div>