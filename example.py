import requests
import json
import os
from dotenv import load_dotenv
from PIL import Image
import base64
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Set API key and organization ID from environment variables
api_key = os.getenv("GROQ_API_KEY")
org_id = os.getenv("GROQ_ORG_ID")

# Set the model and endpoint
model_id = "llama-3.2-90b-vision-preview"
endpoint = "https://api.groq.com/openai/v1/chat/completions"

def extract_characters_from_image(image_path):
    # Open the image file
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Encode the image data as base64
    image_base64 = "data:image/jpeg;base64," + base64.b64encode(image_data).decode("utf-8")
    print(image_base64)
    # Create the request payload
    payload = {
        "model": model_id,
        "messages": [
            {"role": "assistant", "content": {"image": image_base64}},
        ],
        "max_tokens": 1024
    }

    # Set the headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Organization-Id": org_id
    }

    # Send the request
    response = requests.post(endpoint, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 200:
        response_json = response.json()
        text_response = response_json["choices"][0]["message"]["content"]
        return text_response
    else:
        return "Error: Unable to process image"

# Test the function
image_path = "barcode.jpg"
print(extract_characters_from_image(image_path))