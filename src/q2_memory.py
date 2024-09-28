import json
from collections import Counter
from typing import List, Tuple
import re

def count_emojis(content: str) -> Counter:
    """
    This function counts all the emojis found in the provided text.

    Parameters
    ----------
    content : str
        The text where emojis will be searched.

    Returns
    -------
    Counter
        A `Counter` object containing the frequency of each emoji found in the text.
    """
    
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return Counter(emoji_pattern.findall(content))

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    This function analyzes a JSON file line by line to count emojis in the content,
    and returns the 10 most common emojis and their frequency.

    Parameters
    ----------
    file_path : str
        The path to the JSON file to be analyzed.

    Returns
    -------
    List[Tuple[str, int]]
        A list of tuples, where each tuple contains an emoji and its respective frequency of occurrence.
        The list is ordered from most to least frequent and contains only the 10 most common emojis.
    """

    emoji_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:  # Leer línea por línea
            try:
                # Cargar solo el campo 'content' del JSON
                content = json.loads(line).get('content', '')

                # Actualizar el contador de emojis
                emoji_counts.update(count_emojis(content))

            except json.JSONDecodeError:
                # Ignorar líneas que no son JSON válidos
                continue
    
    # TOP 10 emojis más comunes
    top_10_emojis = emoji_counts.most_common(10)

    return top_10_emojis
