# 🛡️ AI-Enhanced Intrusion Detection System

> **Securing Networks Through Artificial Intelligence and Machine Learning.**

---

## 📌 Project Overview

The **AI-Enhanced Intrusion Detection System (IDS)** is a Machine Learning-based Cybersecurity solution designed to detect malicious network activities and identify potential cyber attacks in real time.

This project leverages the **Random Forest Classification Algorithm** trained on the **NSL-KDD Dataset** to analyse network traffic features and classify them as either:

- ✅ **Normal Traffic** — Safe, legitimate network activity
- 🚨 **Attack Traffic** — Malicious or suspicious network behaviour

The application is built using **Python, Flask, Scikit-learn, HTML, CSS, and Bootstrap**, providing an interactive web dashboard for threat analysis and security monitoring.

---

## 👩‍💻 Developer

| Field | Details |
|---|---|
| **Name** | Maithilee Vijay Kale |
| **Roll No** | 20 |
| **PRN No** | 2022011041022 |
| **Degree** | B.Tech – Artificial Intelligence & Machine Learning |
| **University** | D Y Patil Agricultural and Technical University, Talsande, Kolhapur |
| **Academic Year** | 2025-2026 |

---

## 🎯 Objectives

- Detect suspicious network behaviour using Machine Learning.
- Classify network traffic into normal and malicious categories.
- Provide real-time threat analysis through a web interface.
- Demonstrate AI application in Cybersecurity.
- Improve network security monitoring and threat awareness.

---

## 🚀 Features

### 🔹 AI-Powered Threat Detection
Uses a trained Random Forest model to identify cyber threats from network traffic data.

### 🔹 Real-Time Analysis
Users can enter network parameters and instantly receive detection results.

### 🔹 Threat Classification
Classifies traffic as:
- Normal Traffic
- Intrusion Detected

### 🔹 Risk Assessment
Provides risk levels:
- 🟢 **LOW Risk** — Normal traffic
- 🔴 **HIGH Risk** — Attack detected

### 🔹 Threat Analysis Dashboard
Displays:
- Detection Status
- Risk Level
- Threat Type
- Security Recommendations
- Detection Timestamp
- Model Accuracy

### 🔹 Modern Cybersecurity UI
Professional dark-themed dashboard inspired by modern SOC (Security Operations Center) platforms.

---

## 📊 Dataset

### NSL-KDD Dataset

| Parameter | Value |
|---|---|
| Dataset Name | NSL-KDD |
| Total Records | 125,973 |
| Total Features | 43 |
| Type | Balanced (no duplicate records) |
| Attack Categories | DoS, Probe, R2L, U2R |

**Attack Types:**
- **DoS** — Denial of Service attacks
- **Probe** — Surveillance and scanning
- **R2L** — Remote-to-Local unauthorised access
- **U2R** — User-to-Root privilege escalation

---

## 🧠 Machine Learning Model

### Algorithm: Random Forest Classifier

**Why Random Forest?**
- High accuracy on tabular classification tasks
- Handles large datasets efficiently
- Robust against overfitting via ensemble averaging
- Suitable for multi-class classification
- Excellent benchmark performance on NSL-KDD

### Model Performance

| Metric | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Accuracy | **99.85%** |
| Features Used | 43 |
| Dataset | NSL-KDD |

---

## 🏗️ System Architecture

```
Network Traffic Data
        ↓
Feature Extraction & Input Form
        ↓
Data Preprocessing (Encoding, Normalisation)
        ↓
Random Forest Model (ids_model.pkl)
        ↓
Prediction Engine
        ↓
Threat Analysis Dashboard
        ↓
Security Recommendations
```

---

## 🛠️ Technologies Used

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python 3.x | Core programming |
| ML Library | Scikit-learn | Model training & prediction |
| Data Processing | Pandas, NumPy | Data wrangling |
| Model Storage | Joblib | Model serialisation |
| Web Framework | Flask | Backend routing |
| Frontend | HTML5, CSS3 | Page structure & styling |
| UI Components | Bootstrap 5 | Responsive design |
| Dev Tools | VS Code, Jupyter Notebook | Development environment |
| Version Control | GitHub | Source code management |

---

## 📂 Project Structure

```
AI-Enhanced-IDS/
│
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── src/
│   └── main.py                 # ML training pipeline
│
├── models/
│   ├── ids_model.pkl           # Trained Random Forest model
│   ├── protocol_encoder.pkl    # Protocol label encoder
│   ├── service_encoder.pkl     # Service label encoder
│   └── flag_encoder.pkl        # Flag label encoder
│
├── templates/
│   ├── index.html              # Traffic input form
│   └── result.html             # Detection result dashboard
│
├── static/                     # Static assets (CSS, JS, images)
└── dataset/                    # NSL-KDD dataset files
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Enhanced-IDS.git
cd AI-Enhanced-IDS
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model (if not pre-trained)

```bash
python src/main.py
```

### 5. Run the Flask Application

```bash
python app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Sample Test Cases

### ✅ Normal Traffic

| Parameter | Value |
|---|---|
| Duration | 0 |
| Source Bytes | 500 |
| Destination Bytes | 1000 |
| Protocol | TCP |

**Expected Result:**
```
✅ NORMAL TRAFFIC
Risk Level: LOW
```

---

### 🚨 Attack Traffic

| Parameter | Value |
|---|---|
| Duration | 5 |
| Source Bytes | 200,000 |
| Destination Bytes | 800,000 |
| Protocol | UDP |

**Expected Result:**
```
🚨 INTRUSION DETECTED
Risk Level: HIGH
```

---

## 🔒 Cybersecurity Benefits

- Early detection of network intrusions
- Continuous real-time network monitoring
- Supports intrusion prevention workflows
- Raises cybersecurity awareness
- AI-driven intelligent decision making
- Reduces manual monitoring overhead

---

## 🔮 Future Enhancements

- [ ] Deep Learning-based detection (LSTM, CNN)
- [ ] Real-Time Network Packet Capture (Scapy integration)
- [ ] Live network traffic monitoring dashboard
- [ ] SIEM (Security Information & Event Management) Integration
- [ ] Threat Intelligence Feed Integration
- [ ] Advanced attack sub-classification
- [ ] Cloud deployment on AWS / Azure
- [ ] Email & SMS alert notifications
- [ ] Attack visualisation dashboard

---

## 📦 Requirements

```
flask
pandas
numpy
scikit-learn
joblib
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is developed for **educational and academic purposes** as part of the B.Tech curriculum at D Y Patil Agricultural and Technical University.

---

## ⭐ Acknowledgements

- [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html) — Canadian Institute for Cybersecurity
- [Scikit-learn Community](https://scikit-learn.org/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Bootstrap Framework](https://getbootstrap.com/)
- Open Source Cybersecurity Research Community

---

*AI-Enhanced Intrusion Detection System | Maithilee Kale | B.Tech AIML | 2025-2026*