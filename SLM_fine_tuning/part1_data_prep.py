import pandas as pd
import re
import os
from dotenv import load_dotenv
# from groq import Groq
import time
import requests
import json

load_dotenv()

AWANLLM_API_KEY = os.getenv("AWANLLM_API_KEY2")

df_train = pd.read_csv(r"../train_data.csv")

def data_cleaning(input_df):
    """
    Description: this function includes steps to clean up the 'text' field in the dataframe;
    stopword stripping was not used here but in the EDA par
    Parameters: input_df (pd.dataframe)
    Returns: output_df(pd.dataframe)
    """
    
    df_copy = input_df.copy()
    
    # str format control
    df_copy['text'] = df_copy['text'].astype(str) 
    
    # drop duplicates
    df_copy.drop_duplicates(subset='text', inplace=True)
    
    # drop nan
    df_copy.dropna(subset=['text'], inplace=True)
    
    # regex for email addresses
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # filter out emails
    df_copy['text'] = df_copy['text'].apply(lambda x: re.sub(email_regex, '', x))
    
    # filter out comma
    df_copy['text'] = df_copy['text'].str.replace(',', '')
    
    # filter out other punctuations
    df_copy['text'] = df_copy['text'].apply(lambda x: re.sub(r"[^\w\s\(\)']", '', x))

    # filter out some email common vocabs
    df_copy['text'] = df_copy['text'].apply(lambda x: re.sub(r"subject|re ", '', x))
    
    # lowercase
    df_copy['text'] = df_copy['text'].str.lower()
    
    # reset index
    output_df = df_copy[['text']].reset_index(drop=True)

    return output_df

df_cleaned = data_cleaning(df_train)

# only use the first 5k for this project
df_cleaned_5k = df_cleaned.iloc[0:5000]

def labeling_prompt(input_text):

    """
    Description: this function generates email class labels
    Parameters: input_text (str) for one email
    Returns: prompt(str) for complete prompt for class label generation
    """

    prompt =  f""" Your task is to label the text as one of the categories: religion = 1, technology = 2, sports = 3, politics = 4, others = 0
Classify: from (marcus j ranum) subject re text of white house announcement and qas on clipper chip encryption organization trusted information systems inc lines
Answer: 4

Classify: from (seanna (sm) watson) subject re socreligionchristian organization bellnorthern research ottawa canada lines 26 in article (sheila patterson) writes as for the atheistsagnostics who read this list if you aren't christian and if you have no intention of ever becoming one
Answer: 1

Classify: {input_text}
Answer:

Give one number response.
"""
    return prompt

def API_call(prompt):

    """
    Description: sending the prompt to the API
    Parameter: prompt(str)
    Return: an API response object
    """

    url = "https://api.awanllm.com/v1/chat/completions"
    
    # create a formatted payload
    payload = json.dumps({
      "model": "Meta-Llama-3.1-8B-Instruct",
      "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content":prompt}
      ],
      "repetition_penalty": 1.1,
      "temperature": 0.7,
      "top_p": 0.9,
      "top_k": 40,
      "max_tokens": 1024,
      "stream": True
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {AWANLLM_API_KEY}"
    }
    
    response = requests.post(url, headers=headers, data=payload)

    return response

def get_label_from_API(LLM_text):
    """
    Description: this function extracts the label text from the LLAMA3's whole output text
    Parameter: LLM text field from the API response object
    Return: content(str) for class label
    """

    json_strings = LLM_text.split('data: ')[1:-1]
    
    # Parse each JSON string and extract the first content
    for json_str in json_strings:
        data = json.loads(json_str)
        content = data['choices'][0]['delta'].get('content', '')
        if content:
            return content
        
# bulk API calls 
# in the future this code should be concurrently implemented with asyncio and aiohttp
start_time = time.time()

total_rows = len(df_cleaned_5k)
completed_rows = 0

for index, row in df_cleaned_5k.iterrows():
    try:
        response = API_call(labeling_prompt(row['text']))
        label = get_label_from_API(payload.text)

        # make sure label is not null and the API status is 200
        if label is not None and response.status_code == 200:
            df_cleaned_5k.loc[index, "label"] = label
        else:
            # is the label is none or stasus code is wrong, rerun the logic after 10s
            time.sleep(10)
            payload = API_call(labeling_prompt(row['text']))
            label = get_label_from_API(payload.text)
            if label is not None and response.status_code == 200:
                df_cleaned_5k.loc[index, "label"] = label
            
    except Exception as e:
        print(f"An error occurred at row {index}: {e}")
    
    completed_rows += 1
    print(f"Progress: {completed_rows}/{total_rows} done")
    print("---------------")
    
    time.sleep(0.5)

end_time = time.time()

print(f"Total time taken: {end_time - start_time} seconds")

# post labeling cleanup and saving for both training and testing data
df_cleaned_5k.drop('Unnamed: 0')
df_cleaned_5k['text'] = df_cleaned_5k['text'].astype(str)
df_cleaned_5k['label'] = df_cleaned_5k['label'].astype(int)
df_cleaned_5k.to_csv('labeled_data_train.csv')

df_inference = pd.read_csv(r"../test_data.csv")
df_inf = data_cleaning(df_inference)
df_inf['text'] = df_inf['text'].astype(str)
df_inf.to_csv('inference_data.csv')