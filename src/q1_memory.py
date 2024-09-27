from typing import List, Tuple
from datetime import datetime
import json


def get_top_dates(file_path: str) -> List[str]:
    """
    Search for the 10 dates with the most tweets.

    Params
    -------
    file_path (str): path de json.

    Returns
    -------
    Type: string
    Detail: return our date format 'YYYY-MM-DD'.
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
        print(f"Error: Archivo '{file_path}' no encontrado.")
        return []

    except json.JSONDecodeError:
        print(f"Error: Formato de json invalido '{file_path}'.")
        return []

    except Exception as e:
        print(f"Error: {e}")
        return []

def most_username(file_path: str, day: str) -> Tuple[datetime.date, str]:
    """
    Username with the most tweets for our date

    Args
    ------
    file_path (str): path JSON.
    day (str): date in format "YYYY-MM-DD".

    Returns
    ------
    Tupla:
        - date (datetime.date): the date with the most tweets.
        - username (str): the most frequent username for that date.
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
    Return our top 10 dates with the most tweets and the username who tweet the most.

    Args
    -----
    file_path (str): JSON path file.

    Returns
    -----
    Tuple:
        - date (datetime.date): date with the most tweets.
        - username (str): user who tweeted the most for that date.
    """

    days= get_top_dates(file_path)

    return [
        most_username(file_path, day)
        for day in days
    ]