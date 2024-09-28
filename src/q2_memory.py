import json
from collections import Counter
from typing import List, Tuple
import re

def count_emojis(content: str) -> Counter:
    """Generador para contar emojis en el contenido."""
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return Counter(emoji_pattern.findall(content))

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
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
