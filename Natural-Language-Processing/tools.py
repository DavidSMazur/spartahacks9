#imports for tools
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,CallbackManagerForToolRun,)
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import tool

#for knowlege_store
import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import GroundingSource


def knowlege_store():
  vertexai.init(project="euphoric-axiom-412520", location="us-central1")
  parameters = {
      "candidate_count": 1,
      "max_output_tokens": 1024,
      "temperature": 0.9,
      "top_p": 1
  }
  grounding_source = GroundingSource.VertexAISearch(data_store_id="tennis-info_1706390508242", location="global", project="SpartaHack")
  model = TextGenerationModel.from_pretrained("text-bison")
  response = model.predict(
      """""",
      **parameters,
      grounding_source=grounding_source
  )
  print(f"Response from Model: {response.text}")

knowlege_base = StructuredTool.from_function(
    func=knowlege_store,
    name="knowlege_store",
    description="useful for when you need to answer questions about tennis technique, rules, training and strategy",
    # coroutine= ... <- you can specify an async method if desired as well
)
