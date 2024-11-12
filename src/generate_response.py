import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI

def generate_response(prompt, input_variables):
    # Get the Open AI's API key.
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # To initiate the model with temperature and API key.
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # Chain the prompt template and the LLM.
    chain = prompt | llm;

    # Trigger the LLM to generate the response after passing the input variables to the prompt template.
    response = chain.invoke(input_variables)

    return response