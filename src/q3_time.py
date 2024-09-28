import json
import re
from typing import List, Tuple
from collections import Counter

def load_json(file_path: str):
    regex = re.compile(r'@(\w+)')
    mention_count = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            content = json.loads(line).get('content', '')
            mentions = regex.findall(content)
            mention_count.update(mentions)

    return mention_count

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_count = load_json(file_path)

    # Obtener los 10 usuarios más mencionados
    top_users = mention_count.most_common(10)
    return top_users
