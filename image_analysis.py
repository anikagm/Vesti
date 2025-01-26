from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv
import base64
import requests

# Load the API key from the .env file
load_dotenv()  # Load the .env file
groq_api_key = os.environ["GROQ_API_KEY"]

# Initialize the Groq LLM with the 90b-vision-preview model
llm = ChatGroq(
    model_name="llama-3.2-90b-vision-preview",
    temperature=0.7,
    api_key=groq_api_key
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Return the digits displayed in the image."),
    ("user", "Return the digits in {input}. Your output should be a sequence of digits only.")
])

# Define the output parser
parser = JsonOutputParser(pydantic_object={
    "type": "object",
    "properties": {
        "digits": {"type": "number"}
    }
})

# Create the chain that guarantees JSON output
chain = prompt | llm | parser

def analyze_image(image_path: str) -> dict:
    with open(image_path, "rb") as f:
        image_data = f.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")
    result = chain.invoke({"input": encoded_image})
    return result

# Example usage
image_path = "barcode.jpeg"
image_analysis = analyze_image(image_path)
print(image_analysis)