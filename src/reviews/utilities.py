from . import *



def _classify_dataframe(df: pd.DataFrame):
    '''
    Classifies a DataFrame based on specific column presence and modifies the 'provider' column.
    
    Args:
    df (pd.DataFrame): DataFrame to classify.
    
    Raises:
    Exception: If the DataFrame does not match known types or lacks a 'provider' column.
    
    Returns:
    None: Modifies the DataFrame in-place by setting the 'provider' column.
    '''
    if 'provider' not in df.columns:
        df['provider'] = None
    if "event_id" in df.columns and "provider" in df.columns:
        df['provider'] = 'Apple'
    elif "Review Link" in df.columns and "Package Name" in df.columns:
        df['provider'] = 'Google'
    else:
        raise Exception("Unknown Type")
    
    
def _load_csv_from_file(path: str) -> pd.DataFrame:
    """
    Loads a CSV file from the specified  path into a pandas DataFrame
    
    Args:
    path (str): The path of the CSV file.
    
    Returns:
    list: A DataFrame of the CSV file
    """
    try:
        df = pd.read_csv(filepath_or_buffer=path)
    except:
        raise Exception(f"File not found for path: {path}")
    
    
def _load_all_csv_from_folder(path: str = 'data\csv'):
    """
    Loads all CSV files from the specified folder path into a list of pandas DataFrames.
    
    Args:
    path (str): The directory path containing the CSV files.
    
    Returns:
    list: A list containing pandas DataFrames for each CSV file in the directory.
    """
    dataframes = []
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            try:
                file_path = os.path.join(path, filename)
                df = pd.read_csv(file_path)
                dataframes.append(df)
                logging.info(f'Successfully loaded {filename}')
            except pd.errors.EmptyDataError:
                logging.warning(f'{filename} is empty and was skipped.')
            except Exception as e:
                logging.error(f'Failed to read {filename}: {e}')
    return dataframes

def _standardize_time(df: pd.DataFrame):
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df['last_updated'] = df['last_updated'].dt.strftime('%Y-%m-%d %H:%M:%S')

    
def _clean_google_reviews(df: pd.DataFrame):
        print("Cleaning Google reviews...")
        df_new = df.loc[:, ['Review Last Update Date and Time', 'App Version Name',
                     'Star Rating', 
                     'Review Text', 'provider']]
        
        df_new.rename(columns={'Review Text': 'text', 
                            'Review Last Update Date and Time': 'last_updated',
                            'Star Rating': 'rating', 
                            'App Version Name': 'app_version'}, inplace=True)
         # Standardizing time
        _standardize_time(df_new)
        #df_new['rating'] = df_new['rating'].astype(str) + '/5'

        desired_order = ['provider', 'app_version', 'text', 'rating', 'last_updated']
        return df_new[desired_order]

def _clean_apple_reviews(df: pd.DataFrame):
    print("Cleaning Apple reviews...")
    df_new = df.loc[:, ['last_updated', 'app_version',
                     'rating', 
                     'text', 'provider']]
    
    _standardize_time(df_new)
    #df_new['rating'] = df_new['rating'].astype(str) + '/5'
    
    desired_order = ['provider', 'app_version', 'text', 'rating', 'last_updated']
    return df_new[desired_order]

def combine_and_sort_dataframes(cleaned_dfs):
    """
    Concatenates a list of cleaned DataFrames, sorts the resulting DataFrame by 'last_updated',
    and resets the index to ensure it is sequential.
    
    Args:
    cleaned_dfs (list): A list of pandas DataFrames to be combined and sorted.
    
    Returns:
    pandas.DataFrame: A single DataFrame sorted by the 'last_updated' column.
    """
    combined_df = pd.concat(cleaned_dfs)
    sorted_df = combined_df.sort_values(by='last_updated').reset_index(drop=True)
    return sorted_df

def _count_words_in_row(row):
    if pd.notnull(row):
        words = row.split()
        return len(words)
    else:
        return 0

def _drop_short_reviews(df, threshold):
    word_counts = df['text'].apply(_count_words_in_row)
    df = df[word_counts >= threshold]
    return df


def load_and_convert_all_from_folder(folder_path: str = 'data\csv') -> pd.DataFrame:
    """
    Loads, cleans, and combines CSV files from a specified directory into a single DataFrame.

    The function assumes all files are valid CSVs containing app review data from the Google Play Store or the App Store.
    
    Parameters:
    - folder_path (str): The file path to the directory containing the CSV files. Defaults to 'data\csv'.

    Returns:
    - pd.DataFrame: A DataFrame containing the cleaned and combined data from all files. Reviews with less than
      three words or a maximum rating are excluded from the result as they most likely won't contain valueable information.

    Raises:
    - FileNotFoundError: If the specified folder does not exist or is empty.
    - ValueError: If any CSV file does not contain the required 'provider' column or unrecognized provider names.
    - Exception: For any other issues during file loading or processing.
    """
    try:
        dataframes = _load_all_csv_from_folder(folder_path)
        cleaned_dfs = []
        for df in dataframes:
            _classify_dataframe(df)
            provider = df.iloc[0]['provider']
            if provider == 'Apple':
                cleaned_dfs.append(_clean_apple_reviews(df))
            elif provider == 'Google':
                cleaned_dfs.append(_clean_google_reviews(df))
            else:
                raise Exception("Unknown Type")
        combined_df = combine_and_sort_dataframes(cleaned_dfs)
        combined_df = _drop_short_reviews(combined_df, 3)
        combined_df = combined_df[combined_df['rating'] < 5]
        return combined_df
        
    except Exception as e:
        print(f"An error occurred: {e}")
        