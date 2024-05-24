from . import *
from .models import *
from tqdm import tqdm
import pandas as pd



def summarize_list(review_list: list, model, prompt_str):
    result_string = '\n'.join(review_list)
    prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Reviews: {result_string}")])
    try:
        result = query_model(model=model, prompt=prompt)
    except Exception as e:
        print(f"An error occurred: {e}")
    return result

def predict_text(column, model, prompt_str) -> pd.Series:
    """_summary_

    Args:
        column (_type_): Pandas DataFrame column
        model (_type_): A defined language model
        prompt_str (_type_): The prompt, should predict a generated text or pre-defined non-binary tag.

    Returns:
        _type_: A new column with the predicted values
    """
    results = pd.Series(index=column.index, dtype=object)
    for index, text in tqdm(column.items(), total=len(column), desc="Generating text predictions..."):
        prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {text}")])
        try:
            results.at[index] = query_model(model=model, prompt=prompt)
        except Exception as e:
            print(f"An error occurred at index {index}: {e}")
    
    return results
        

def predict_binary(texts, model, prompt_str) -> pd.Series:
    """_summary_

    Args:
        column (_type_): Pandas DataFrame column
        model (_type_): A defined language model
        prompt_str (_type_): The prompt, should predict a generated text or pre-defined non-binary tag.

    Returns:
        _type_: A new column with the predicted values
    """
    results = pd.Series(index=texts.index, dtype=bool)
    try:
        for index, text in tqdm(texts.items(), total=len(texts), desc="Predicting usable reviews..."):
            prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {text}")])
            answer = query_model(model=model, prompt=prompt)
            results.at[index] = 'True' in answer
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return results