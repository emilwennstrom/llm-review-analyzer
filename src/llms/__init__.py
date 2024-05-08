from langchain_google_vertexai import ChatVertexAI, VertexAIModelGarden, VertexAI, VertexAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_URL = os.getenv('OLLAMA_URL')
LOCATION = os.getenv('LOCATION')
PROJECT = os.getenv('PROJECT')

