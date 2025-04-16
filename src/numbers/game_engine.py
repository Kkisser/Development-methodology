import game1
import game2

def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game_rules: str, generate_round: Callable[[], Tuple[str, str]], name: str, rounds: int = 3) -> None:
    """
    Основной движок игры
    :param game_rules: Правила игры для показа пользователю
    :param generate_round: Функция генерации раунда (возвращает вопрос и правильный ответ)
    :param name: Имя игрока
    :param rounds: Количество раундов (по умолчанию 3)
    """
    print(game_rules)

    for _ in range(rounds):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
