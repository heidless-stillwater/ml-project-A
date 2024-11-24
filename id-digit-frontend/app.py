import streamlit as st
import requests

st.title('My First Streamlit App')

st.write('Welcome to my Streamlit app!')

user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

st.write('Customized Message:', user_input)

API='https://id-digit-backend-svc-394099236728.europe-west2.run.app'
#
# API='http://localhost:5000/'

resp = requests.post(API, files={'file': open('test/eight.png', 'rb')})

answer_json = resp.json()
answer = answer_json['prediction']

st.write("prediction: ", answer)
st.write(resp.json())

# st.write(answer)

# st.header("END")

