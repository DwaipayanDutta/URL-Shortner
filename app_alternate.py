import streamlit as st
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def main():
    st.set_page_config(page_title="URL Shortener", page_icon=":link:")
    st.title("URL Shortener")

    url = st.text_input("Enter the URL to shorten:")

    if st.button("Shorten"):
        if url:
            short_url = shorten_url(url)
            st.success(f"Shortened URL: {short_url}")
        else:
            st.warning("Please enter a URL.")

    st.write("---")
    st.markdown("## About")
    st.write("This is a simple URL shortener built using Streamlit and PyShorteners.")
    st.write("Enter a URL in the input field and click the 'Shorten' button to get a shortened version of the URL.")

if __name__ == "__main__":
    main()