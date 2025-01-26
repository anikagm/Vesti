import base64
import requests
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()  # Load the .env file

groq_api_key = os.environ["GROQ_API_KEY"]
print(groq_api_key)  # Print the API key

# Load the image file
with open("barcode.jpg", "rb") as f:
    image_data = f.read()

# Compress the image file
compressed_image = base64.b64encode(image_data)

# Set the API endpoint and model ID
api_endpoint = "https://api.groq.com/openai/v1/chat/completions"
model_id = "llama-3.2-90b-vision-preview"

# Set the request payload
payload = {
    "model": model_id,
    "messages": [
        {"role": "user", "content": "Analyze the text in the image"},
        {"role": "image", "content": compressed_image.decode("utf-8")}
    ]
}

# Set the headers
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.post(api_endpoint, headers=headers, json=payload)

# Get the response text
response_text = response.json()["choices"][0]["message"]["content"]

print(response_text)