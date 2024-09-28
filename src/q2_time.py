import json
from collections import Counter
from typing import List, Tuple
import re

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Finds the top 10 most common emojis in a JSON file containing text data.

    Parameters
    ----------
    file_path : str
        The path to the JSON file containing text data in each line.

    Returns
    -------
    List[Tuple[str, int]]
        A list of tuples, each containing:
        - str: The emoji character.
        - int: The count of occurrences of that emoji in the text data.
    """

    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    emoji_counts = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line).get('content', '')
                
                for emoji in emoji_pattern.findall(data):
                    emoji_counts[emoji] += 1

            except json.JSONDecodeError:
                continue
    
    top_10_emojis = emoji_counts.most_common(10)
    
    return top_10_emojis