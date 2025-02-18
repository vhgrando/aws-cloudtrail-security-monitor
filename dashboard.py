import streamlit as st
import pandas as pd
import requests

# Set Page Title
st.set_page_config(page_title="AWS CloudTrail Security Dashboard", layout="wide")

# API Endpoint (Replace with your actual API Gateway URL)
API_URL = "https://lk30vn6thh.execute-api.us-east-1.amazonaws.com/prod/logs"

# Function to fetch logs from API
def fetch_logs():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return pd.DataFrame(response.json())  # Convert JSON response to DataFrame
        else:
            st.error(f"⚠️ Failed to fetch logs: {response.status_code}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"⚠️ API Request Failed: {e}")
        return pd.DataFrame()

# Load data
df = fetch_logs()

# Title
st.title("🚀 AWS CloudTrail Security Dashboard")

# Display recent security logs
st.subheader("📜 Recent Security Events")

if not df.empty:
    # Convert RiskLevel to readable format
    df["RiskLevel"] = df["RiskLevel"].replace({"🚨 CRITICAL": "Critical", "⚠️ MEDIUM": "Medium", "🔎 LOW": "Low"})

    # Filter options
    risk_filter = st.radio("🔍 Filter by Risk Level:", ["All", "Critical 🚨", "Medium ⚠️", "Low 🔎"])

    if risk_filter == "Critical 🚨":
        df = df[df["RiskLevel"].str.contains("Critical")]
    elif risk_filter == "Medium ⚠️":
        df = df[df["RiskLevel"].str.contains("Medium")]
    elif risk_filter == "Low 🔎":
        df = df[df["RiskLevel"].str.contains("Low")]

    # Display the security events as a table
    st.dataframe(df[["Timestamp", "RiskLevel", "User", "Action"]], height=400)

else:
    st.success("✅ No suspicious activity detected.")

# Add a refresh button
if st.button("🔄 Refresh Logs"):
    st.experimental_rerun()
