from typing import List, Tuple
from datetime import datetime
import pandas as pd
import statistics
import json


def read_json(file_path: str) -> pd.DataFrame:
    """
    Reads a JSON file, then returns a Dataframe using pandas.

    Args
    ------
    file_path (str): the path to the JSON file.

    Returns
    ------
    df (DataFrame): a pandas DataFrame containing the data from the JSON file.
    """
    days = []
    usernames = []

    with open(file_path, 'r') as f:
        for line in f:
            tweet= json.loads(line)
            days.append(tweet['date'])
            usernames.append(tweet['user']['username'])

    df = pd.DataFrame()
    df["day"]= days
    df["username"]= usernames

    return df

def format_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the date column of a pandas DataFrame.

    Args
    -----
    df (DataFrame): Dataframe format from pandas.

    Returns
    -----
    df (DataFrame): return column formatted in pandas Dataframe.
    """

    df["day"]= df.day.apply(
        lambda x: datetime.strptime(x.split("T")[0], "%Y-%m-%d").date()
    )
    return df

def get_data(df: pd.DataFrame) -> Tuple[List[datetime.date], List[str]]:
    """
    Top 10 dates with most tweets and username with the most tweets those dates.

    Args
    -----
    df (DataFrame): the pandas DataFrame to use in the analysis.

    Returns:
    Tuple in its 2 columns:
        - days (List[datetime.date]): Top 10 dates with the most tweets.
        - users (List[str]): User who tweeted the most in those dates.
    """
    # Get ocurrences by date & most frequent username
    df= df.groupby("day").agg([
        ('count', 'count'), 
        ('username', lambda x: statistics.mode(x))
    ])

    # Get top 10 days
    df= df.sort_values(
        by= [('username', 'count')], ascending=False
    ).head(10)

    days, users= df.index.tolist(), df.username.username.tolist()
    
    return list(zip(days, users))

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Returns the top 10 days with the most occurrences and the most frequent username.

    Args
    -----
    file_path (str): the path to the JSON file.

    Returns
    -----
    Tuple in its 2 columns:
        - days (List[datetime.date]): Top 10 dates with the most tweets.
        - users (List[str]): User who tweeted the most in those dates.
    """
    try:
        tweets = read_json(file_path)
        tweets = format_date(tweets)
        return get_data(tweets)
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return []
    
    except Exception as e:
        print(f"Error: {e}")
        return []