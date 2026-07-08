import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
df = pd.read_csv("dataset/Courier_Delivery_Dataset.csv")

# Label Encoders
pickup_encoder = LabelEncoder()
destination_encoder = LabelEncoder()
courier_encoder = LabelEncoder()

df["Pickup_Location"] = pickup_encoder.fit_transform(df["Pickup_Location"])
df["Destination"] = destination_encoder.fit_transform(df["Destination"])
df["Courier_Type"] = courier_encoder.fit_transform(df["Courier_Type"])

# Features
X = df[
    [
        "Pickup_Location",
        "Destination",
        "Courier_Type",
        "Historical_Deliveries"
    ]
]

# Target
y = df["Actual_Delivery_Days"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "models/courier_model.pkl")

joblib.dump(pickup_encoder, "models/pickup_encoder.pkl")
joblib.dump(destination_encoder, "models/destination_encoder.pkl")
joblib.dump(courier_encoder, "models/courier_encoder.pkl")

print("Model trained successfully!")