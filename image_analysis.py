from langchain_groq import ChatGroq
import langchain_core
import os
from dotenv import load_dotenv
import base64
from groq import Groq
  
# Load the API key from the .env file
load_dotenv()  # Load the .env file

groq_api_key = os.environ["GROQ_API_KEY"]

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image(image_path):
    llm = ChatGroq(
        model_name="llama-3.2-90b-vision-preview",
        temperature=0.7,
    )
  
    client = Groq(api_key=os.environ['GROQ_API_KEY'])

    base64_image = encode_image(image_path)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Return the brand and material content depicted on this apparel tag. Your output should be two values in the following format, with no additional text or symbols: Prada, 100% Acetate"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )

    results = chat_completion.choices[0].message.content
    results_list = results.split(", ") # list: brand, material
    return results_list

brand = analyze_image("example_tag_picture.jpg")
print(brand)
