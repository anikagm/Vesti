from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

# API key: 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

load_dotenv()  # Load the .env file

groq_api_key = os.environ["GROQ_API_KEY"]

def get_brand_info(brand_name):

    # Initialize Groq LLM
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )

    # Define the expected JSON structure
    parser = JsonOutputParser(pydantic_object={
        "type": "object",
        "properties": {
            "rating": {"type": "number"},
            "details": {"type": "string"
                # "type": "array",
                # "items": {"type": "string"}
            },
            "different brands": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    })

    # Create a simple prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Extract product details into JSON with this structure:
            {{
                "rating": number_here_without_currency_symbol,
                "details": "description of about three sentences here",
                "different brands": ["brand1", "brand2", "brand3"]
            }}"""),
        ("user", "{input}")
    ])

    # Create the chain that guarantees JSON output
    chain = prompt | llm | parser

    # future idea: run an if statement...if brand is more than 8/10 rating, no need to suggest more brands
    description = f"Rate the apparel brand {brand_name} out of ten for sustainability and humanitarianism. Then suggest a few apparel brans which are more sustainable but still within the same price range."

    result = chain.invoke({"input": description})
    rating = result['rating']
    details = result['details']
    diff_brands = result['different brands']

    print(f"Rating: {rating}/10 \nDetails: {details} \nDifferent Brands to Consider: {diff_brands}")
