import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("phishing_model.pkl")

st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Phishing Website Detection")
st.markdown("### Machine Learning Based Website Security Scanner")
st.write("Enter the feature values below and click **Predict**.")

feature_names = [
"URLLength",
"DomainLength",
"IsDomainIP",
"URLSimilarityIndex",
"CharContinuationRate",
"TLDLegitimateProb",
"URLCharProb",
"TLDLength",
"NoOfSubDomain",
"HasObfuscation",
"NoOfObfuscatedChar",
"ObfuscationRatio",
"NoOfLettersInURL",
"LetterRatioInURL",
"NoOfDegitsInURL",
"DegitRatioInURL",
"NoOfEqualsInURL",
"NoOfQMarkInURL",
"NoOfAmpersandInURL",
"NoOfOtherSpecialCharsInURL",
"SpacialCharRatioInURL",
"IsHTTPS",
"LineOfCode",
"LargestLineLength",
"HasTitle",
"DomainTitleMatchScore",
"URLTitleMatchScore",
"HasFavicon",
"Robots",
"IsResponsive",
"NoOfURLRedirect",
"NoOfSelfRedirect",
"HasDescription",
"NoOfPopup",
"NoOfiFrame",
"HasExternalFormSubmit",
"HasSocialNet",
"HasSubmitButton",
"HasHiddenFields",
"HasPasswordField",
"Bank",
"Pay",
"Crypto",
"HasCopyrightInfo",
"NoOfImage",
"NoOfCSS",
"NoOfJS",
"NoOfSelfRef",
"NoOfEmptyRef",
"NoOfExternalRef"
]

values = []

col1, col2 = st.columns(2)

for i, feature in enumerate(feature_names):
    if i % 2 == 0:
        with col1:
            val = st.number_input(feature, value=0.0)
    else:
        with col2:
            val = st.number_input(feature, value=0.0)

    values.append(val)

if st.button("🔍 Predict Website"):

    input_df = pd.DataFrame([values], columns=feature_names)

    prediction = model.predict(input_df)[0]

    st.divider()

    if prediction == 1:
        st.error("🚨 This Website is PHISHING")
    else:
        st.success("✅ This Website is LEGITIMATE")


    
