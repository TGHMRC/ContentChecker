import streamlit as st
import tempfile
import os
from govuk_checker import check_html, check_docx

st.title("GOV.UK Style & Content Checker")

uploaded_file = st.file_uploader("Upload an HTML or DOCX file", type=["htm", "html", "docx"])

if uploaded_file:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    ext = os.path.splitext(tmp_path)[1].lower()
    if ext in [".htm", ".html"]:
        findings = check_html(tmp_path)
    elif ext == ".docx":
        findings = check_docx(tmp_path)
    else:
        findings = ["Unsupported file type."]

    st.subheader("Findings")
    if findings:
        for f in findings:
            st.write(f)
        st.write(f"**Total findings:** {len(findings)}")
    else:
        st.write("No issues found.")

    os.remove(tmp_path)
