import streamlit as st
from pdf_reader import extract_text
from resume_analyzer import analyze_resume

st.set_page_config(
    page_title="Thiru Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume in PDF format.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
job_description = st.text_area(
    "Paste Job Description (Optional)",
    height=200,
    placeholder="Paste the job description here..."
)

if uploaded_file is not None:

    with st.spinner("Reading Resume..."):
        resume = extract_text(uploaded_file)

    st.success("Resume extracted successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):
            result = analyze_resume(resume)

        st.markdown("## Analysis Report")
        st.markdown(result)

        st.download_button(
            "Download Report",
            result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )