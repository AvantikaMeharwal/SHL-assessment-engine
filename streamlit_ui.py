# streamlit_ui.py

import streamlit as st
import requests

st.title("SHL Assessment Recommender")

job_role = st.text_input("Enter Job Role")
skills = st.text_input("Enter Key Skills (comma separated)")

if st.button("Recommend"):
    query = f"{job_role} {skills}"
    try:
        response = requests.post("http://127.0.0.1:8000/recommend", json={"query": query})
        if response.status_code == 200:
            data = response.json()
            if data:
                st.success("Recommendations found:")
                st.table(data)
            else:
                st.warning("No recommendations found.")
        else:
            st.error("Error calling the API.")
    except Exception as e:
        st.error(f"API call failed: {e}")
