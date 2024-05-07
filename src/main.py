from llms.models import *
from llms.prompts import *
from langchain_core.prompts import ChatPromptTemplate





model = chat_bison()
prompt = ChatPromptTemplate.from_messages([("system", usable_review_binary_prompt), ("human", f"Tänk om man kunde spara sina fakturor offline")])
answer = query_model(model=model, prompt=prompt)

print(answer)