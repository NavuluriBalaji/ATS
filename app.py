from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash
import base64
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
# app.secret_key = 'your_secret_key'

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() 
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your summary on the candidate's profile. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        uploaded_file = request.files['uploaded_file']
        action = request.form['action']

        if uploaded_file:
            pdf_content = input_pdf_setup(uploaded_file)
            if action == 'summarize':
                response = get_gemini_response(input_prompt1, pdf_content, input_text)
            elif action == 'match':
                response = get_gemini_response(input_prompt3, pdf_content, input_text)
            flash(response, 'info')
        else:
            flash('Please upload the resume', 'error')
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        input_text = request.form['input_text']
        uploaded_file = request.files['uploaded_file']
        action = request.form['action']

        if uploaded_file:
            pdf_content = input_pdf_setup(uploaded_file)
            if action == 'summarize':
                response = get_gemini_response(input_prompt1, pdf_content, input_text)
            elif action == 'match':
                response = get_gemini_response(input_prompt3, pdf_content, input_text)
            flash(response, 'info')
        else:
            flash('Please upload the resume', 'error')
        return redirect(url_for('form'))
    return render_template('form.html')

@app.route('/coming-soon')
def coming_soon():
    return render_template('coming_soon.html')

if __name__ == '__main__':
    app.run(debug=True)
