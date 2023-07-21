import requests
from langchain.tools import BaseTool
from .base import extract_name
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import ChatPromptTemplate
from .base import _JSON_TO_NLG_RESPONSE_TEMPLATE

# Define the API endpoint
API_ENDPOINT = "https://api.genderize.io/"

class GenderizeTool(BaseTool):
    def __init__(self):
        super().__init__(name="genderize", description="Predicts the gender of a person.")

    def _run(self, input_text: str) -> str:
        # Extract name of person from the input text
        name = extract_name(input_text)
        # Call the genderize.io API with the provided name
        response = requests.get(API_ENDPOINT, params={"name": name})
        # Check if the API call was successful
        if response.status_code == 200:
            # Parse the JSON response and extract the age
            data = response.json()
            prompt = ChatPromptTemplate.from_template(_JSON_TO_NLG_RESPONSE_TEMPLATE)
            llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
            chain = LLMChain(
                llm=llm,
                prompt=prompt
            )
            """
            Sample json output:
            {"count":1094417,"name":"michael","gender":"male","probability":1.0}
            Generated NLG response:
            The name is Michael and it is a male name. The probability of it being a male name is 1.0.
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
# input_text = "What can be the gender of  Michael?"
# tool = NationaliseTool()
# result = tool.run(input_text)
# print(result)