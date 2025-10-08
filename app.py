import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Netflix Sentiment App", page_icon="🎬")

st.title("🎬 Netflix Reviews Sentiment Analysis")
st.write("Explore user sentiments from Netflix app reviews.")

# Example: Load model & dataset (if available)
# model = joblib.load("models/sentiment_model.joblib")
# df = pd.read_csv("data/cleaned_reviews.csv")

# Simple interactive example
user_input = st.text_area("Paste a Netflix app review here:")
if st.button("Analyze Sentiment"):
    st.success("Sentiment: Mildly Positive ✅")  # placeholder for real prediction
