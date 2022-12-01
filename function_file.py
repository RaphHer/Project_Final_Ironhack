# Function created to clean the Capital IQ files 

import pandas as pd 
from functools import reduce # will be used to merge all the df


def clean_CapIQ (df_name):
    df_name.dropna(inplace=True) # Get rid of Nan Values
    df_name.rename(columns={'Unnamed: 0': 'Period',
                              'Unnamed: 1': 'Value',
                            'Unnamed: 2' : 'Simple Growth Rate %',
                            'Unnamed: 3' : 'Y-o-Y Change %',
                            'Unnamed: 4' : 'Annual % Rate',
                            'Unnamed: 5' : 'Type'},
                              inplace=True, errors='raise') # Rename the column with the right name
    df_name = df_name.drop([df_name.index[0]]) # Drop the row with the column name
    df_name.reset_index(drop=True, inplace=True) # Reset the index 
    df_name.drop(['Type', 'Simple Growth Rate %', "Y-o-Y Change %", "Annual % Rate"], axis = 1, inplace = True) # Delete columns  
    df_name['Period'] = df_name['Period'].apply(lambda x: x.strftime('%Y-%m')) # Removing the days that we don't need (for the record it was end of the month value)
    df_name['Period'] = pd.to_datetime(df_name['Period']) # Putting back the day so we have beginning of the month everywhere
    return df_name

def clean_Refinitiv(df_name):
    df_name.rename(columns={'First Release Data': 'Period',
                         'Unnamed: 1' : 'Original Release Date',
                        'Unnamed: 2': 'First Release'},
                              inplace=True, errors='raise') # Rename the column with the right name
    df_name.drop(index=[0,1,2], inplace=True) # Drop the row with the column name
    df_name.dropna(inplace=True) # Get rid of Nan Values 
    df_name.reset_index(drop=True, inplace=True) # Reset the index 
    df_name['First Release'] = df_name['First Release'].astype(float) # Transform the object number to a normal float
    df_name["Period"] = pd.to_datetime(df_name["Period"]) # Transform the date
    df_name.drop(["Original Release Date"], axis=1, inplace=True) # Drop the release date column that is unecessary
    return df_name

def clean_df(df_name, column_name):
    df_name.reset_index(inplace=True)  # reset the index to access in the second step the date
    df_name[column_name] = df_name[column_name].apply(lambda x: x.strftime('%Y-%m')) # removing the days that we don't need (for the record it was end of the month value)
    df_name[column_name] = pd.to_datetime(df_name[column_name]) # putting back the day so we have beginning of the month everywhere
    return df_name

 def prophet_pred (ticker, date):
    df = yf.download(ticker, start=date)
    df = df.reset_index()
    df [['ds','y']] = df[['Date','Adj Close']]
    return df


