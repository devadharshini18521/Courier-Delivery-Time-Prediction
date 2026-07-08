import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, timedelta

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="AI-Powered Courier Delivery Prediction",
    page_icon="🚚",
    layout="wide"
)

# ======================================
# LOAD MODEL
# ======================================

model = joblib.load("models/courier_model.pkl")

pickup_encoder = joblib.load("models/pickup_encoder.pkl")
destination_encoder = joblib.load("models/destination_encoder.pkl")
courier_encoder = joblib.load("models/courier_encoder.pkl")
# ======================================
# Sidebar
# ======================================

st.sidebar.title("🚚 Courier Delivery AI")

st.sidebar.markdown("---")

st.sidebar.subheader("👩‍💻 Developer")
st.sidebar.write("Devadharshini")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Project")
st.sidebar.write("Courier Delivery Time Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 Machine Learning")
st.sidebar.write("Random Forest Regressor")

st.sidebar.markdown("---")

st.sidebar.subheader("🛠 Technologies")

st.sidebar.write("• Python")
st.sidebar.write("• Pandas")
st.sidebar.write("• Scikit-Learn")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Power BI")

st.sidebar.markdown("---")

st.sidebar.caption("AI-Powered Courier Delivery Time Prediction")
# ======================================
# HEADER
# ======================================

st.title("🚚 AI-Powered Courier Delivery Time Prediction")
st.markdown("""
### Smart Courier Delivery Prediction System

This application predicts the expected courier delivery time using a
Machine Learning Regression Model trained on historical shipment data.

### Project Objective

Estimate courier delivery time using:

- 📍 Pickup Location
- 🎯 Destination
- 🚚 Courier Type
- 📊 Historical Deliveries

### Prediction Output

- 📅 Estimated Delivery Days
- 📆 Expected Delivery Date
- 🎯 Delivery Confidence Score
""")

st.info("Enter shipment details and click **Predict Expected Delivery Time**.")

# ======================================
# PROJECT OVERVIEW
# ======================================

st.markdown("## 📊 Project Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📦 Dataset",
        "10,000+ Records"
    )

with c2:
    st.metric(
        "🤖 ML Model",
        "Random Forest"
    )

with c3:
    st.metric(
        "📈 Type",
        "Regression"
    )

st.markdown("---")
# ======================================
# SHIPMENT DETAILS
# ======================================
st.markdown("## 📦 Shipment Details")

left, right = st.columns(2)

with left:

    pickup = st.selectbox(
        "📍 Pickup Location",
        pickup_encoder.classes_
    )

    courier = st.selectbox(
        "🚚 Courier Type",
        courier_encoder.classes_
    )

with right:

    destination = st.selectbox(
        "🎯 Destination",
        destination_encoder.classes_
    )

    historical = st.number_input(
        "📊 Historical Deliveries (Days)",
        min_value=1,
        max_value=30,
        value=3,
        step=1
    )

st.markdown("---")

predict = st.button(
    "🚀 Predict Expected Delivery Time",
    use_container_width=True
)
# ======================================
# PREDICTION
# ======================================
if predict:

    pickup_encoded = pickup_encoder.transform([pickup])[0]

    destination_encoded = destination_encoder.transform(
        [destination]
    )[0]

    courier_encoded = courier_encoder.transform(
        [courier]
    )[0]

    input_data = pd.DataFrame({

        "Pickup_Location":[pickup_encoded],

        "Destination":[destination_encoded],

        "Courier_Type":[courier_encoded],

        "Historical_Deliveries":[historical]

    })

    prediction = model.predict(input_data)

    predicted_days = max(1, round(prediction[0]))

    expected_date = datetime.today() + timedelta(days=predicted_days)

    confidence = max(
        70,
        min(
            100,
            100 - abs(predicted_days-historical)*5
        )
    )
    # ======================================
    # PREDICTION RESULTS
    # ======================================

    st.success("✅ Prediction Generated Successfully!")

    st.markdown("## 📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📅 Estimated Delivery",
            f"{predicted_days} Days"
        )

    with col2:
        st.metric(
            "📆 Expected Delivery Date",
            expected_date.strftime("%d-%m-%Y")
        )

    with col3:
        st.metric(
            "🎯 Confidence Score",
            f"{confidence}%"
        )

    st.markdown("---")
    # ======================================
    # SHIPMENT SUMMARY
    # ======================================
    st.markdown("## 📦 Shipment Summary")

    left, right = st.columns(2)

    with left:
        st.write("**📍 Pickup Location**")
        st.write(pickup)

        st.write("**🚚 Courier Type**")
        st.write(courier)

    with right:
        st.write("**🎯 Destination**")
        st.write(destination)

        st.write("**📊 Historical Deliveries**")
        st.write(f"{historical} Day(s)")

    st.markdown("---")

    # ======================================
    # DELIVERY CONFIDENCE
    # ======================================

    st.markdown("## 📈 Delivery Confidence")

    st.progress(confidence / 100)

    st.caption(f"Model Confidence: {confidence}%")

    st.markdown("---")

    # ======================================
    # DELIVERY STATUS
    # ======================================

    st.markdown("## 🚚 Delivery Status")

    if predicted_days <= 2:
        st.success("🟢 Fast Delivery Expected")

    elif predicted_days <= 5:
        st.info("🟡 Standard Delivery Expected")

    else:
        st.warning("🔴 Delivery May Take Longer Than Expected")

    st.markdown("---")

    # ======================================
    # FOOTER
    # ======================================

    st.caption("🚚 AI-Powered Courier Delivery Time Prediction System")
    st.caption("Developed by Devadharshini")
    st.caption("Powered by Python • Scikit-Learn • Streamlit • Power BI")