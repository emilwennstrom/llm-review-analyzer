from . import *
from .models import *
from tqdm import tqdm
import pandas as pd



def text_prediction(column, model, prompt_str):
    """_summary_

    Args:
        column (_type_): Pandas DataFrame column
        model (_type_): A defined language model
        prompt_str (_type_): The prompt, should predict a generated text or pre-defined non-binary tag.

    Returns:
        _type_: A new column with the predicted values
    """
    results = pd.Series(index=column.index, dtype=object)
    for index, text in tqdm(column.items(), total=len(column), desc="Processing..."):
        prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {text}")])
        try:
            results.at[index] = query_model(model=model, prompt=prompt)
        except Exception as e:
            print(f"An error occurred at index {index}: {e}")
    
    return results
        
def predict_binary_single_model(df_orig, model, prompt_str) -> pd.DataFrame:
    df = df_orig.copy()
    try:
        df['usable'] = None
        for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing... "):
            prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {row['text']}")])
            answer = query_model(model=model, prompt=prompt)
            if 'True' in answer:
                df.at[index, 'usable'] = True
            else:
                df.at[index, 'usable'] = False
        return df
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        

def predict_binary_single_column(texts, model, prompt_str) -> pd.Series:
    results = pd.Series(index=texts.index, dtype=bool)
    try:
        for index, text in tqdm(texts.items(), total=len(texts), desc="Processing..."):
            prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {text}")])
            answer = query_model(model=model, prompt=prompt)
            results.at[index] = 'True' in answer
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return results

        
def predict_binary_multiple_models(df, models, prompt_str):
    try:
        for model_name, model in models:
            df[model_name + '_usable'] = None
            print(f"Calling: {model_name}")
            for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing {model_name}", leave=False):
                prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {row['text']}")])
                answer = query_model(model=model, prompt=prompt)
                if 'True' in answer:
                    df.at[index, model_name + "_usable"] = True
                else:
                    df.at[index, model_name + "_usable"] = False
        return df     
    except KeyError:
        print("Error: The DataFrame does not contain a 'text' column.")
    except Exception as e:
        print(f"An error occurred: {e}")