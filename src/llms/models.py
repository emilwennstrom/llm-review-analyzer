from . import *

"""
    Define more models according to needs
"""


def query_model(model, prompt):
    chain = prompt | model | StrOutputParser()
    answer = chain.invoke({})
    return answer

def llama3_ollama(temperature = 0, top_k = 10, top_p = 0.5):
    return Ollama(
        name='llama3:instruct',
        base_url=OLLAMA_URL,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )

def chat_bison(temperature = 0, top_k = 10, top_p = 0.5):
    return ChatVertexAI(
            model_name="chat-bison",
            location=LOCATION,
            project=PROJECT,
            max_output_tokens=1024,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
    )
    
def text_bison(temperature = 0, top_k = 10, top_p = 0.5):
    return VertexAI(
            model_name="text-bison",
            location=LOCATION,
            project=PROJECT,
            max_output_tokens=1024,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
    )
    
    
def get_models(include_chat_bison = False, include_text_bison = False, include_llama3 = False):
    '''
        For fetching multiple models at the same time if
        tests on different models want to be done.
    '''
    models = []
    if include_chat_bison:
        models.append(['chat_bison', chat_bison()])
    if include_text_bison:
        models.append(['text_bison', text_bison()])
    if include_llama3:
        models.append(['llama3', llama3_ollama()])
    return models