import streamlit as st
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

st.title("URL Shortener")

url = st.text_input("Enter the URL to shorten:")

if st.button("Shorten"):
    if url:
        short_url = shorten_url(url)
        st.success(f"Shortened URL: {short_url}")
    else:
        st.warning("Please enter a URL.")