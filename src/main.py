from llms.models import *
from llms.prompts import *
from reviews.utils import load_and_convert_all


def main():
    
    '''
        Load CSV-File from file
    '''
    dataframe = load_and_convert_all()
    
    try:
        for index, row in dataframe.iterrows():
            print(index, row['text'])  # Accessing the 'text' column of each row
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    
    
    
    #model = chat_bison()
    #prompt = ChatPromptTemplate.from_messages([("system", usable_review_binary_prompt), ("human", f"Tänk om man kunde spara sina fakturor offline")])
    #answer = query_model(model=model, prompt=prompt)

    #print(answer)

if __name__ == "__main__":
    main()