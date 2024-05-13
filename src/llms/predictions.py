from . import *
from .models import *
from tqdm import tqdm
import pandas as pd



def topic_analysis(df_orig, model, prompt_str):
    df = df_orig.copy()
    try:
        df['topic'] = None
        for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Processing... "):
            prompt = ChatPromptTemplate.from_messages([("system", prompt_str), ("human", f"Review: {row['text']}")])
            df.at[index, 'topic'] = query_model(model=model, prompt=prompt)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        
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