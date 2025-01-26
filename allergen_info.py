from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

# API key: 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

load_dotenv()  # Load the .env file

groq_api_key = os.environ["GROQ_API_KEY"]

def allergen_details(product_type, material_content):
    # Initialize Groq LLM
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )

    # Define the expected JSON structure
    parser = JsonOutputParser(pydantic_object={
        "type": "object",
        "properties": {
            "allergens": {
                "type": "array",
                "items": {"type": "string"}
            },
            "associated hazards": {"type": "string"}
        }
    })

    # Create a simple prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Extract product details into JSON with this structure:
            {{
                "allergens": ["allergen1", "allergen2", "allergen3"]
                "associated hazards": "associated health hazards here in 5 sentences maximum"
            }}"""),
        ("user", "{input}")
    ])

    # Create the chain that guarantees JSON output
    chain = prompt | llm | parser

    description = f"Given {product_type} with {material_content}, list all possible allergens or irritants in the apparel item. Also list any health hazards associated with each possible allergen."

    result = chain.invoke({"input": description})
    allergens = result['allergens']
    hazards = result['associated hazards']
    
    print(f"Allergens: {allergens}\nHealth hazards:\n  {hazards}")