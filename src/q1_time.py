from typing import List, Tuple
from datetime import datetime
import pandas as pd
import statistics
import json


def read_json(file_path: str) -> pd.DataFrame:
    """
    Reads a JSON file and returns a DataFrame using pandas.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the data from the JSON file,
        with columns 'day' for the date and 'username' for the user who tweeted.
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
    Formats the 'day' column of a pandas DataFrame to datetime.date objects.

    Parameters
    ----------
    df : pd.DataFrame
        The pandas DataFrame with a 'day' column in string format.

    Returns
    -------
    pd.DataFrame
        The modified DataFrame with the 'day' column formatted as datetime.date.
    """

    df["day"]= df.day.apply(
        lambda x: datetime.strptime(x.split("T")[0], "%Y-%m-%d").date()
    )
    return df

def get_data(df: pd.DataFrame) -> Tuple[List[datetime.date], List[str]]:
    """
    Finds the top 10 dates with the most tweets and the most active usernames on those dates.

    Parameters
    ----------
    df : pd.DataFrame
        The pandas DataFrame containing tweet data with columns 'day' and 'username'.

    Returns
    -------
    Tuple[List[datetime.date], List[str]]
        A tuple containing:
        - List[datetime.date]: Top 10 dates with the most tweets.
        - List[str]: Usernames of the users who tweeted the most on those dates.
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
    Returns the top 10 dates with the most tweets and the most frequent usernames for those dates.

    Parameters
    ----------
    file_path : str
        The path to the JSON file containing tweet data.

    Returns
    -------
    List[Tuple[datetime.date, str]]
        A list of tuples, where each tuple contains:
        - datetime.date: The date with the most tweets.
        - str: The username of the user who tweeted the most on that date.
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