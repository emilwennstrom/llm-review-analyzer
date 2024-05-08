from langchain_google_vertexai import ChatVertexAI, VertexAIModelGarden, VertexAI, VertexAIEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

ollama_url = os.getenv('OLLAMA_URL')
location = os.getenv('LOCATION')
project = os.getenv('PROJECT')

