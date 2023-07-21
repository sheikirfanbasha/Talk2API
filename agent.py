from langchain.agents import Agent
from tools.nationaliseTool import NationaliseTool
from tools.agifyTool import AgifyTool
from tools.genderizeTool import GenderizeTool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
talk2APIAgent = initialize_agent([
    NationaliseTool(),
    AgifyTool(),
    GenderizeTool()
], llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
    
# Example Usage
# input_text = "What is the age of Michael?"
# input_text = "What can be the gender of  Michael?"
# input_text = "What can be the nationality of  Michael?"
# result = talk2APIAgent.run(input_text)
# print(result)