from . import *


def predict_binary_single_model(df, model, prompt_str):
    try:
        for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing... "):
            prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {row['text']}")])
            answer = query_model(model=model, prompt=prompt)
            if 'True' in answer:
                df.at[index, 'prediction'] = True
            else:
                df.at[index, 'prediction'] = False
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def predict_binary_multiple_models(df, models, prompt_str):
    try:
        for model_name, model in models:
            print(f"Calling: {model_name}")
            for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing {model_name}", leave=False):
                prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {row['text']}")])
                answer = query_model(model=model, prompt=prompt)
                if 'True' in answer:
                    df.at[index, model_name + "_prediction"] = True
                else:
                    df.at[index, model_name + "_prediction"] = False
                
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    
    # Load CSV-Files from folder
    df = load_and_convert_all_from_folder()
    
    
    
    
    # Single model
    predict_binary_single_model(df=df, model=chat_bison(), prompt_str=usable_review_binary_prompt)
    
    print(df.head())


    
    #models = get_models(include_chat_bison=True, include_text_bison=True)
    #predict_multiple_models(models=models)
    
        
        
    #print(df[df['chat_bison_prediction'] != df['text_bison_prediction']])
    
    

    
if __name__ == "__main__":
    main()