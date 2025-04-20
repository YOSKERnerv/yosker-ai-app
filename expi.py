import requests

url = "https://your-colab-url.ngrok.io/predict"
data = {"example_input": "test data"}

try:
    response = requests.post(url, json=data)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)
