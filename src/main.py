import matplotlib.pyplot as plt
from langchain_community.document_loaders import DataFrameLoader
from llms.predictions import *
from llms.prompts import *
from gcloud.translate_utilities import *
from gcloud.storage_utilities import *
from reviews.utilities import *
from tqdm.auto import tqdm
from vectors.clustering import cluster_reviews
import pandas as pd



LOAD_FROM_BUCKET = True
MODEL = chat_bison()
TRANSLATE_REVIEWS = True



def main():
    
    df_orig = None
    # Load data from either file or bucket
    if (LOAD_FROM_BUCKET is False):
        df_orig = load_and_convert_all_from_folder(folder_path='data/fake_reviews')
    else:
        df_orig = load_and_convert_from_bucket()
        print(df_orig.head())
        #list_blobs_in_bucket()
        
    
    
    
    
    
    if df_orig is None:
        raise ValueError("DataFrame is empty or not loaded properly")

    # Translate reviews
    df = df_orig.copy()
    column_to_use = 'translated' if TRANSLATE_REVIEWS else 'text'
    
    if (TRANSLATE_REVIEWS):
        tqdm.pandas(desc="Translating texts")
        df['translated'] = df['text'].progress_apply(apply_translation)
    
    # Predict usable reviews
    df['usable'] = predict_binary(texts=df[column_to_use], model=MODEL, prompt_str=usable_review_binary_prompt)
    df = df[df['usable'] == True]
    df.drop('usable', axis=1, inplace=True)
    
    # Predict if either a bug report or feature request
    df['predicted'] = predict_text(column=df[column_to_use], model=MODEL, prompt_str=bug_or_feature_prompt)
    
    df['cluster_id'] = cluster_reviews(review_column=df[column_to_use], translated=TRANSLATE_REVIEWS)
    
    print(df.head())
    
    
    
    return
    
        
    # Calculate moving average
    df_orig['moving_avg'] = df_orig['rating'].rolling(window=7).mean()  # 7-day moving average
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot your data
    ax.plot(df_orig['last_updated'], df_orig['moving_avg'], label='Moving Average')

    # Select a subset of dates for x-axis ticks
    ticks = df_orig['last_updated'][::30]  # Select every 30th date; adjust the stride as needed

    # Set the ticks on the x-axis
    ax.set_xticks(ticks)
    ax.set_xticklabels([t.strftime('%Y-%m-%d') for t in ticks], rotation=45)

    # Set the labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Rating')
    ax.set_title('Moving Average of App Reviews')
    ax.grid(True)
    ax.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


        
    
if __name__ == "__main__":
    main()