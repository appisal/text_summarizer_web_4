import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download NLTK Punkt Tokenizer
nltk.download("punkt", quiet=True)

# Function to summarize text
def summarize_text(text, num_sentences):
    # Parse the text using PlaintextParser and Tokenizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    # Generate the summary with the specified number of sentences
    summary = summarizer(parser.document, num_sentences)
    summarized_text = " ".join(str(sentence) for sentence in summary)
    return summarized_text

# Streamlit App
st.title("Text Summarizer")

# Section to Upload a Text File
st.write("Upload a .txt file or paste your text below to summarize it.")

uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("Original Text", value=text, height=200)

    # Select Number of Sentences for Summary
    num_sentences = st.slider("Number of sentences for the summary:", 1, 10, 3)

    # Generate and Display Summary
    if st.button("Summarize"):
        summary = summarize_text(text, num_sentences)
        st.subheader("Summary:")
        st.write(summary)
else:
    # Text Input Section for Copy-Pasting Text
    text = st.text_area("Paste your text here:", height=200)
    num_sentences = st.slider("Number of sentences for the summary:", 1, 10, 3)

    # Generate and Display Summary
    if st.button("Summarize"):
        if text.strip():
            summary = summarize_text(text, num_sentences)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please paste some text or upload a file to summarize.")

