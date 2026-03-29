# AI Resume Screening System

## What This Project Does
The **AI Resume Screening System** is a Python-based web application that automates resume screening. It:
- Extracts text from PDF resumes.
- Scores resumes based on required skills.
- Ranks candidates automatically.
- Highlights the best candidate.


## Setup Instructions

1. **Clone the repository**
https://github.com/princymhjn-beep/Resume-Screening-System.git

2. **Create a virtual environment**
[ python -m venv venv ]

Activate the virtual environment: Windows: [ venv\Scripts\activate ]

3. **Install required libraries**
[ pip install streamlit PyPDF2 ]

4. **Run the application**
[ streamlit run main.py ]


## How to Use

Open the Streamlit app in your browser.
Enter the required skills (comma-separated), e.g.:
Python, SQL, Machine Learning
Upload one or more PDF resumes.
Click “Screen Resumes”.
View the results:
  1. Ranked candidate list
  2. Score for each candidate
  3. Skills found
  4. Best candidate highlighted at the top


## Sample Output

| Candidate Name | Score | Skills Found                  |
| -------------- | ----- | ----------------------------- |
| John_Doe.pdf   | 5     | Python, SQL, Machine Learning |
| Jane_Smith.pdf | 3     | Python, SQL, Machine Learning |

Best Candidate: John_Doe.pdf


## Technologies Used
Python 3.8+
Streamlit (Web interface)
PyPDF2 (PDF text extraction)


## Future Enhancements
Add support for DOCX and other file formats.
Use NLP to analyze context and experience.
Build analytics dashboard for skills and candidate comparison.
Integrate with email/job portals for full automation.


