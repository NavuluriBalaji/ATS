
# ATS Resume Builder & Analyzer

### Overview

The ATS Resume Scanner is a tool designed to help job seekers optimize their resumes for specific job descriptions. By leveraging the Gemini 1.5 Flash model, this tool compares the content of a resume with the provided job description and calculates the percentage match. Additionally, it provides actionable suggestions to enhance the resume, ensuring a higher compatibility with Applicant Tracking Systems (ATS).


## Features

- Percentage Match Calculation: Automatically calculates how well your resume matches a given job description.
- Actionable Suggestions: Provides specific recommendations on how to update your resume to better align with the job description.
- User-Friendly Interface: Easy-to-use interface for uploading resumes and job descriptions.
- Advanced NLP Model: Utilizes the powerful Gemini 1.5 Flash model for accurate and reliable analysis.


## Technology Used

- Gemini 1.5 Flash Model: For advanced natural language processing.
- Streamlit
## Getting Started

- Clone the repository: git clone https://github.com/NavuluriBalaji/ATS.git
- Navigate to the project directory: cd ats-resume-scanner
- Install the required dependencies: pip install -r requirements.txt
- Replace GOOGLE_API_KEY="Your_API_Key" with your Gemini Api Key in ".env" File (You can generate your API Key Here: https://makersuite.google.com)
- Run the application: python app.py
- Open your browser and go to http://localhost:5000 to start using the tool.
