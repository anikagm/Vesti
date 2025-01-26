from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# import json
from dotenv import load_dotenv
import os

# API key: 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

load_dotenv()  # Load the .env file

groq_api_key = os.environ["GROQ_API_KEY"]
print(groq_api_key)  # Print the API key

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Define the expected JSON structure
parser = JsonOutputParser(pydantic_object={
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "price": {"type": "number"},
        # "features": {
        #     "type": "array",
        #     "items": {"type": "string"}
        # }
    }
})

# Create a simple prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """Extract product details into JSON with this structure:
        {{
            "name": "product name here",
            "price": number_here_without_currency_symbol,
            "features": ["feature1", "feature2", "feature3"]
        }}"""),
    ("user", "{input}")
])

# Create the chain that guarantees JSON output
chain = prompt | llm | parser

def parse_product(description: str) -> None:
    result = chain.invoke({"input": description})
    name = result['name']
    price = result['price']
    return name, price

# Example usage
description = """The Kees Van Der Westen Speedster is a high-end, single-group espresso machine known for its precision, performance, 
and industrial design. Handcrafted in the Netherlands, it features dual boilers for brewing and steaming, PID temperature control for 
consistency, and a unique pre-infusion system to enhance flavor extraction. Designed for enthusiasts and professionals, it offers 
customizable aesthetics, exceptional thermal stability, and intuitive operation via a lever system. The pricing is approximatelyt $14,499 
depending on the retailer and customization options."""

name_and_price_list = parse_product(description)
print(name_and_price_list[0], " + $", name_and_price_list[1])