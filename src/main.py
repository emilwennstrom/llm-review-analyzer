from llms.models import *
from llms.prompts import *
from reviews.utils import load_and_convert_all
from tqdm import tqdm


def main():
    
    '''
        Load CSV-File from file
    '''
    df = load_and_convert_all()
    
    
    '''
     Single model
    '''
    # Single    
    '''try:
        for index, row in dataframe.iterrows():
            print(row['text'], row['rating'])
            prompt = ChatPromptTemplate.from_messages([("system", usable_review_binary_prompt), ("human", f"Review: {row['text']}")])
            answer = query_model(model=chat_bison(), prompt=prompt)
            print(answer)
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")'''
        
    '''Multiple models'''
    
    models = get_models(include_chat_bison=True, include_text_bison=True)
    
    try:
        for model_name, model in models:
            print(f"Calling: {model_name}")
            for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing {model_name}", leave=False):
                prompt = ChatPromptTemplate.from_messages([("system", usable_review_binary_prompt), ("human", f"Review: {row['text']}")])
                answer = query_model(model=model, prompt=prompt)
                if 'True' in answer:
                    df.at[index, model_name] = True
                else:
                    df.at[index, model_name] = False
                
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
    print(df[df['chat_bison'] != df['text_bison']])
    
    

    
if __name__ == "__main__":
    main()