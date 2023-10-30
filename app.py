import streamlit as st
import requests
import json
from decouple import config

my_url = config('MY_URL')   

# st.title("QnATables: An Intelligent Question Answering System")
st.markdown("<h1 style='font-size:28px;'>QnATables: An Intelligent Question Answering System</h1>", unsafe_allow_html=True)
# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
if st.button("Upload") and uploaded_file is not None:
    url = f"{my_url}upload"
    files = {"file": ("file.pdf", uploaded_file.read(), "application/pdf")}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        st.write("File uploaded successfully!")
    else:
        st.write("Error uploading file.")

user_question = st.text_input("Enter your question here:")
if st.button("Submit") and user_question:
    url = f"{my_url}answer"
    question = user_question
    payload = {'text': user_question}
    response = requests.request("POST", url, data=payload)
    print(response)
    try:
        response_data = response.json()['ans']  
        st.write("Answer:", response_data)
    except json.JSONDecodeError as e:
        st.write("Error decoding JSON response:", str(e))
