import joblib
import pandas as pd

# Load trained model
model = joblib.load("../models/ids_model.pkl")

# Load test dataset
df = pd.read_csv(
    r"C:\Users\sayal\PycharmProjects\AI_Enhanced_Intrusion_Detection_System\data\KDDTest+.txt",
    header=None
)

# Remove label column (41) and difficulty column (42)
X = df.iloc[:, :-2]

# Predict
predictions = model.predict(X)

print("First 20 Predictions:")
print(predictions[:20])