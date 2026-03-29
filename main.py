import streamlit as st
from PyPDF2 import PdfReader

# Title
st.title(" AI Resume Screening System")

# Input for required skills
skills_input = st.text_input("Enter required skills (comma separated):")
REQUIRED_SKILLS = [skill.strip().lower() for skill in skills_input.split(",") if skill]

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

# Function to extract text
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content.lower()
    
    return text

# Function to score resume
def score_resume(text):
    score = 0
    found_skills = []

    for skill in REQUIRED_SKILLS:
        if skill in text:
            score += 1
            found_skills.append(skill)

    return score, found_skills

# Process button
if st.button("Screen Resumes"):
    results = []

    if uploaded_files and REQUIRED_SKILLS:
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            score, skills = score_resume(text)

            results.append({
                "name": file.name,
                "score": score,
                "skills": skills
            })

        # Sort results
        results.sort(key=lambda x: x["score"], reverse=True)

        st.subheader("Results")

        for i, res in enumerate(results, start=1):
            st.write(f"**{i}. {res['name']}**")
            st.write(f"Score: {res['score']}")
            st.write(f"Skills Found: {', '.join(res['skills'])}")
            st.write("---")

        #  Best Candidate
        if results:
            st.success(f" Best Candidate: {results[0]['name']}")

    else:
        st.warning("Please upload resumes and enter skills.")
