import streamlit as st
import pandas as pd
from PIL import Image

# Load Data
df = pd.read_csv('product_catalogue.csv')

# Add Logo (Center Aligned)
image = Image.open('logo.png')
st.image(image, width=200)

# Main Title & Subheading
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>SHL Assessment Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Get the Best Assessment Based on Your Requirement</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for User Input
st.sidebar.header("Search Recommendation")
query = st.sidebar.text_input("Enter your requirement:")

# Search Logic
if query:
    result = df[df['Description'].str.contains(query, case=False)]
    if not result.empty:
        st.subheader("Recommended Assessments")
        for index, row in result.iterrows():
            with st.container():
                st.markdown(f"### {row['Assessment']}")
                st.markdown(f"**Description:** {row['Description']}")
                st.markdown(f"**Category:** {row['Category']}")
                st.markdown("---")
    else:
        st.warning("No matching assessment found!")
else:
    st.info("Please enter a search query in sidebar.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Powered by SHL Assessment Engine</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by: Varda Hanwant ❤️</p>", unsafe_allow_html=True)
