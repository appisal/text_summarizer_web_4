import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit App
st.title("Text Summarizer")

# Instructions for the user
st.write("Upload a text file or paste your text below to summarize it.")

# File Upload Section
uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("Original Text", value=text, height=200)

    # Slider to select the number of words in the summary
    num_words = st.slider("Maximum words for the summary:", 50, 500, 100)

    # Generate and Display Summary
    if st.button("Summarize"):
        if len(text.split()) < 10:
            st.warning("The text is too short to summarize. Please provide more content.")
        else:
            summary = summarizer(text, max_length=num_words, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.write(summary[0]["summary_text"])
else:
    # Text Input Section
    text = st.text_area("Paste your text here:", height=200)
    num_words = st.slider("Maximum words for the summary:", 50, 500, 100)

    # Generate and Display Summary
    if st.button("Summarize"):
        if len(text.split()) < 10:
            st.warning("The text is too short to summarize. Please provide more content.")
        else:
            summary = summarizer(text, max_length=num_words, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.write(summary[0]["summary_text"])
