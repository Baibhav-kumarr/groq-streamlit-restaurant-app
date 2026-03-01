import streamlit as st
import langchainhelper

st.title("🍽️ Restaurant Idea Generator")

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["Italian", "Chinese", "Mexican", "Indian", "French"]
)

if cuisine:
    response = langchainhelper.generate_restaurant_idea(cuisine)

    st.header(response["restaurant_name"])

    for item in response["menu_items"]:
        st.write(f"- {item}")