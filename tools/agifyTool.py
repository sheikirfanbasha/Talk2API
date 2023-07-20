import requests
from langchain.tools import BaseTool
from base import extract_name

# Define the API endpoint
API_ENDPOINT = "https://api.agify.io"

class AgifyTool(BaseTool):
    def __init__(self):
        super().__init__(name="agify", description="Returns the age of a person.")

    def _run(self, input_text: str) -> str:
        # Extract name of person from the input text
        name = extract_name(input_text)
        # Call the Agify.io API with the provided name
        response = requests.get(API_ENDPOINT, params={"name": name})

        # Check if the API call was successful
        if response.status_code == 200:
            # Parse the JSON response and extract the age
            data = response.json()
            age = data.get("age")

            # Return the age as a string
            return f"{name} is {age} years old."
        else:
            # Return an error message if the API call failed
            return "Error: Failed to retrieve age information."
        
    async def _arun(
        self
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

# Example usage
# input_text = "What is the age of Michael?"
# tool = AgifyTool()
# result = tool.run(input_text)
# print(result)