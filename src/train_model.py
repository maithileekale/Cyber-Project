import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# =========================
# Dataset Column Names
# =========================

columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes',
    'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised',
    'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files',
    'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
    'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate',
    'dst_host_srv_serror_rate',
    'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'label',
    'difficulty'
]

# =========================
# Load Dataset
# =========================

df = pd.read_csv(
    r"C:\Users\sayal\PycharmProjects\AI_Enhanced_Intrusion_Detection_System\data\KDDTrain+.txt",
    names=columns
)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# Label Encoding
# =========================

protocol_encoder = LabelEncoder()
service_encoder = LabelEncoder()
flag_encoder = LabelEncoder()
label_encoder = LabelEncoder()

df['protocol_type'] = protocol_encoder.fit_transform(df['protocol_type'])
df['service'] = service_encoder.fit_transform(df['service'])
df['flag'] = flag_encoder.fit_transform(df['flag'])
df['label'] = label_encoder.fit_transform(df['label'])

print("\nEncoded Data:")
print(df.head())

# =========================
# Save Encoders
# =========================

joblib.dump(protocol_encoder, "../models/protocol_encoder.pkl")
joblib.dump(service_encoder, "../models/service_encoder.pkl")
joblib.dump(flag_encoder, "../models/flag_encoder.pkl")
joblib.dump(label_encoder, "../models/label_encoder.pkl")

print("\nEncoders Saved Successfully!")

# =========================
# Features and Target
# =========================

X = df.drop('label', axis=1)
y = df['label']

# =========================
# Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =========================
# Model Training
# =========================

print("\nTraining Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# Prediction
# =========================

predictions = model.predict(X_test)

# =========================
# Accuracy
# =========================

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(accuracy)

# =========================
# Classification Report
# =========================

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# =========================
# Confusion Matrix
# =========================

cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)

# =========================
# Save Model
# =========================

joblib.dump(model, "../models/ids_model.pkl")

print("\nModel Saved Successfully!")

# =========================
# Accuracy Graph
# =========================

plt.figure(figsize=(6, 4))
plt.bar(["Random Forest"], [accuracy])
plt.title("AI-Enhanced IDS Accuracy")
plt.ylabel("Accuracy Score")
plt.ylim(0.90, 1.00)

plt.savefig("../results/accuracy.png")

print("\nAccuracy Graph Saved!")

plt.show()

# =========================
# Confusion Matrix Graph
# =========================

ConfusionMatrixDisplay.from_predictions(
    y_test,
    predictions
)

plt.savefig("../results/confusion_matrix.png")

print("\nConfusion Matrix Graph Saved!")

plt.show()

print("\nProject Execution Completed Successfully!")