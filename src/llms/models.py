from . import *
from langchain_google_vertexai import ChatVertexAI, VertexAIModelGarden, VertexAI, VertexAIEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

def query_model(model, prompt):
    chain = prompt | model
    answer = chain.invoke({})
    if (isinstance(model, ChatVertexAI)):
        return answer.content
    else:
        return answer


def chat_bison(temperature = 0, top_k = 10, top_p = 0.5):
    print(location, project)
    return ChatVertexAI(
            model_name="chat-bison",
            location=location,
            project=project,
            max_output_tokens=1024,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
    )