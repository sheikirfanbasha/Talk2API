from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatOpenAI
schema = {
    "properties": {
        "name": {"type": "string"}
    },
    "required": ["name"],
}
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
# Define the extraction chain to extract the name of the person from user input
extraction_chain = create_extraction_chain(schema, llm, verbose=True)
def extract_name(input_text: str) -> str:
    """Extracts the name from the input text."""
    extracted_result = extraction_chain.run(input_text)
    name = extracted_result[0]["name"]
    return name
_JSON_TO_NLG_RESPONSE_TEMPLATE = """Given the data in the json output. 
Generate the human readable response.
json output:
{input}
"""