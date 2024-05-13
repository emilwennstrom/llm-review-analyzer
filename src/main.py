import matplotlib.pyplot as plt
from langchain_community.document_loaders import DataFrameLoader
import pandas as pd
from llms.predictions import *
from llms.prompts import *
from reviews.utilities import *



def main():
    '''choice = ''
    while choice.lower() != 'q':
        df = None
        print("Handle reviews from folder or bucket?")
        print("1 - Folder")
        print("2 - Bucket")
        print("q - Quit")
        choice = input()  # Get user input
        if choice == '1':
            print("Handling folder...")
            df = load_and_convert_all_from_folder()
        elif choice == '2':
            # Code to handle the bucket case
            print("Handling bucket...")
        elif choice.lower() == 'q':
            print("Quitting...")
            df = None
            break
        else:
            print("Invalid choice, please enter 1, 2, or q.")

        if df is None: continue
        # Single model
        df = predict_binary_single_model(df_orig=df[:10], model=chat_bison(), prompt_str=usable_review_binary_prompt)
        
        print(df.head())'''

    df_orig = load_and_convert_all_from_folder()
    if df_orig is None:
        raise ValueError("DataFrame is empty or not loaded properly")

    print(df_orig['last_updated'])
    #models = get_models(include_chat_bison=True, include_text_bison=True)
    #predict_multiple_models(models=models)
    
    df = predict_binary_single_model(df_orig=df_orig, model=chat_bison(), prompt_str=usable_review_binary_prompt)
    df = df[df['usable'] == True]
    df.drop('usable', axis=1, inplace=True)
    df = topic_analysis(df_orig=df, model=chat_bison(), prompt_str=topics_prompt)
        
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