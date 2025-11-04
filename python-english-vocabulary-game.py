
words_easy = {
    "new": "новый",
    "old": "старый",
    "people": "люди",
    "hand": "рука",
    "minute": "минута"  
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открыть",
    "think": "думать"
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",  
    "except": "кроме"
}


levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}


def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Сложный")
    choice = input("Введите выбор: ").strip().lower()
    
    if "легк" in choice or "1" in choice:
        return words_easy
    elif "средн" in choice or "2" in choice:
        return words_medium
    elif "сложн" in choice or "3" in choice:
        return words_hard
    else:
        print("Некорректный выбор. Используем средний уровень.")
        return words_medium


def play_game(words):
    answers = {}
    for eng_word, rus_word in words.items():
        print(f"\nВыбран уровень. Подберите перевод для: {eng_word}")
        print(f"Длина слова: {len(rus_word)} букв, начинается на '{rus_word[0]}'")
        
        user_ans = input("Ваш перевод: ").strip().lower()
        
        if user_ans == rus_word.lower():  
            print(f"Верно! {eng_word.title()} - это {rus_word}")
            answers[eng_word] = True
        else:
            print(f"Неверно. {eng_word.title()} - это {rus_word}")
            answers[eng_word] = False
    
    return answers

# Отображение результатов
def display_results(answers):
    correct = [word for word, correct in answers.items() if correct]
    incorrect = [word for word, correct in answers.items() if not correct]
    
    result = ""
    if correct:
        result += "Правильно отвечены слова:\n" + "\n".join(correct) + "\n"
    if incorrect:
        result += "Неправильно отвечены слова:\n" + "\n".join(incorrect)
    return result


def calculate_rank(answers):
    correct_count = sum(1 for correct in answers.values() if correct)
    return levels.get(correct_count, "Неизвестно")


def main():
    words = choose_difficulty()
    answers = play_game(words)
    print("\nРезультаты теста:")
    print(display_results(answers))
    print(f"Ваш рейтинг: {calculate_rank(answers)}")

if __name__ == "__main__":
    main()