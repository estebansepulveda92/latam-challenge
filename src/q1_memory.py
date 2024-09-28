from typing import List, Tuple
from datetime import datetime
import json
from memory_profiler import profile


def get_top_dates(file_path: str) -> List[str]:
    """
    Searches for the top 10 dates with the most tweets in a JSON file.

    Parameters
    ----------
    file_path : str
        The path to the JSON file containing tweet data.

    Returns
    -------
    List[str]
        A list of strings representing the top 10 dates (in 'YYYY-MM-DD' format)
        with the highest number of tweets.
    """
    tweets_by_date= {}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                tweet= json.loads(line)
                day= tweet['date'].split("T")[0]
                tweets_by_date[day]= tweets_by_date.get(day, 0) + 1

        # TOP 10
        return [
            day for day, _ in sorted(
                tweets_by_date.items(), key=lambda x: x[1], reverse=True
            )[:10]
        ]

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

    except json.JSONDecodeError:
        print(f"Error: Invalid file type '{file_path}'.")
        return []

    except Exception as e:
        print(f"Error: {e}")
        return []

def most_username(file_path: str, day: str) -> Tuple[datetime.date, str]:
    """
    Finds the username with the most tweets on a given date.

    Parameters
    ----------
    file_path : str
        The path to the JSON file containing tweet data.
    day : str
        The date in 'YYYY-MM-DD' format for which to find the top username.

    Returns
    -------
    Tuple[datetime.date, str]
        A tuple containing:
        - date (datetime.date): The date for which the most active username is found.
        - username (str): The username with the highest number of tweets on that date.
    """
    usernames = {}
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                tweet= json.loads(line)

                if tweet['date'].split("T")[0]== day:
                    usernames[tweet['user']['username']]= usernames.get(
                        tweet['user']['username'], 0
                    ) +1
        
        day = datetime.strptime(day, "%Y-%m-%d").date()

        return (day, max(usernames, key=usernames.get))

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return (None, None)

    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return (None, None)

    except Exception as e:
        print(f"Error: {e}")
        return (None, None)

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Returns the top 10 dates with the most tweets and the username 
    with the highest number of tweets on those dates.

    Parameters
    ----------
    file_path : str
        The path to the JSON file containing tweet data.

    Returns
    -------
    List[Tuple[datetime.date, str]]
        A list of tuples, each containing:
        - date (datetime.date): The date with the most tweets.
        - username (str): The username with the most tweets on that date.
    """

    days= get_top_dates(file_path)

    return [
        most_username(file_path, day)
        for day in days
    ]