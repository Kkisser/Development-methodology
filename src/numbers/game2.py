import random
from typing import Tuple, Callable

def generate_progression_round() -> Tuple[str, str]:
    """Генерация раунда для игры Прогрессия"""
    progression = generate_geometric_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer

def generate_geometric_progression() -> list[int]:
    """Генерирует геометрическую прогрессию"""
    start = random.randint(1, 5)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    return [start * (step ** i) for i in range(length)]
