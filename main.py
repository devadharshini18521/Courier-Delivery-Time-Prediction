import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("Courier_Cleaned_Dataset.csv")

# Encode categorical columns
le = LabelEncoder()

df["Origin"] = le.fit_transform(df["Origin"])
df["Destination"] = le.fit_transform(df["Destination"])
df["Mode"] = le.fit_transform(df["Mode"])
df["Nature of Consignment"] = le.fit_transform(df["Nature of Consignment"])

# Features
X = df[
    [
        "Origin",
        "Destination",
        "Chargeable Wt",
        "Mode",
        "Nature of Consignment"
    ]
]

# Target
y = df["Historical_Delivery_Days"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Check error
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", mae)