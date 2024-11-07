import streamlit as st
import requests

import requests

st.title('My First Streamlit App')

st.write('Welcome to my Streamlit app!')


# Define the API endpoint
url = 'https://get-estimate-394099236728.europe-west2.run.app'

resp = requests.post(url, files={'file': open('three.png', 'rb')})

print("json received: ", resp.json())

result = resp.json()
st.header("These headers have rotating dividers", divider=True)

pred = result['prediction']
pred_s = pred.str()
st.write('streamlit:', pred_s)

user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

st.write('Customized Message:', user_input)

resp = requests.post(url, files={'file': open('three.png', 'rb')})

# Make the API call
# response = requests.get('https://my-prediction-394099236728.europe-west2.run.app')

# Display the response in the app
st.write(resp.json())

# api results

# user_input1 = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# st.write('API Result:', user_input1)

