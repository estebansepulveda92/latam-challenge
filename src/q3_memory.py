import json
from typing import List, Tuple
from collections import Counter, defaultdict
import re


def load_json(file_path: str):
    regex = re.compile(r'@(\w+)')
    mention_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            content = json.loads(line).get('content', '')
            mentions = regex.findall(content)
            for username in mentions:
                mention_count[username] += 1

    return mention_count
    

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_count = load_json(file_path)
    
    # Convert to a sorted list of tuples and get the top 10
    top_users = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_users