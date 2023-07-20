import requests
from langchain.tools import BaseTool
from base import extract_name
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import ChatPromptTemplate

_NATIONALISE_RESPONSE_TEMPLATE = """Given the data in the json output. 
Generate the human readable response.
json output:
{input}
"""

# Define the API endpoint
API_ENDPOINT = "https://api.nationalize.io/"

class NationaliseTool(BaseTool):
    def __init__(self):
        super().__init__(name="nationalise", description="Predicts the nationality of a person.")

    def _run(self, input_text: str) -> str:
        # Extract name of person from the input text
        name = extract_name(input_text)
        # Call the nationalise.io API with the provided name
        response = requests.get(API_ENDPOINT, params={"name": name})
        # Check if the API call was successful
        if response.status_code == 200:
            # Parse the JSON response and extract the age
            data = response.json()
            prompt = ChatPromptTemplate.from_template(_NATIONALISE_RESPONSE_TEMPLATE)
            llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
            chain = LLMChain(
                llm=llm,
                prompt=prompt
            )
            """
            Sample json output:
            {"count":2101006,"name":"michael","country":[{"country_id":"AT","probability":0.061},{"country_id":"DE","probability":0.056},{"country_id":"DK","probability":0.054},{"country_id":"IE","probability":0.048},{"country_id":"GH","probability":0.046}]}
            Generated NLG response:
            The name is Michael and there are a total of 2,101,006 occurrences of this name. The name is most likely associated with the following countries and their respective probabilities: Austria (0.061), Germany (0.056), Denmark (0.054), Ireland (0.048), and Ghana (0.046).
            """
            return chain.run(input=data)
        else:
            # Return an error message if the API call failed
            return "Error: Failed to retrieve age information."
        
    async def _arun(
        self
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

# Example usage
# input_text = "What can be the nationality of  Michael?"
# tool = NationaliseTool()
# result = tool.run(input_text)
# print(result)