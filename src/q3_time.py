import json
import re
from typing import List, Tuple
from collections import Counter

def load_json(file_path: str):
    """
    Loads a JSON file and counts the number of user mentions (@username) in the 'content' field of each line.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    Returns
    -------
    mention_count : Counter
        A Counter object where keys are usernames (str) mentioned in the content and values are the number of times each username was mentioned (int).
    """
    
    regex = re.compile(r'@(\w+)')
    mention_count = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            content = json.loads(line).get('content', '')
            mentions = regex.findall(content)
            mention_count.update(mentions)

    return mention_count

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Finds the top 10 most mentioned users in the content of a JSON file.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    Returns
    -------
    List[Tuple[str, int]]
        A list of tuples, each containing:
        - str: The username that was mentioned.
        - int: The number of times that username was mentioned.
    """

    mention_count = load_json(file_path)

    # Obtener los 10 usuarios más mencionados
    top_users = mention_count.most_common(10)
    return top_users
