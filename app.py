import streamlit as st
import requests
from config import api_key, search_engine_id  # Import API key and search engine ID

# Function to fetch data from Google Custom Search API
def fetch_data(query):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results

# Streamlit app
st.title("Web Data Retriever")
query = st.text_input("Enter your query:")
submit = st.button("submit")

if submit:
    results = fetch_data(query)
    if "items" in results:
        for item in results["items"]:
            st.write(f"**{item['title']}**")
            st.write(item['link'])
            st.write("---")
    else:
        st.write("No results found.")
