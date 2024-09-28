import json
from collections import Counter
from typing import List, Tuple
import re

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Regex para detectar emojis en el rango Unicode extendido
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    
    # Crear el contador de emojis
    emoji_counts = Counter()
    
    # Cargar el archivo JSON en modo iterativo
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:  # Leer línea por línea
            try:
                # Cargar el JSON línea por línea
                data = json.loads(line).get('content', '')
                
                # Encontrar y contar emojis directamente
                for emoji in emoji_pattern.findall(data):
                    emoji_counts[emoji] += 1

            except json.JSONDecodeError:
                # Ignorar líneas que no son JSON válidos
                continue
    
    # TOP 10 emojis más comunes
    top_10_emojis = emoji_counts.most_common(10)
    
    return top_10_emojis