print("hi")
import random

def get_categories():
    return [
        "ארץ",
        "עיר",
        "חי",
        "צומח",
        "דומם",
        "שם פרטי",
        "מאכל",
        "מקצוע"
    ]

def get_random_letter():
    # Hebrew letters commonly used in ארץ עיר
    letters = [
        'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ',
        'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת'
    ]
    return random.choice(letters)

def play_game():
    print("ברוכים הבאים למשחק ארץ-עיר!")
    categories = get_categories()
    letter = get_random_letter()
    print(f"האות שלך היא: {letter}")
    answers = {}
    for category in categories:
        answer = input(f"{category} המתחיל באות {letter}: ")
        answers[category] = answer

    print("\n--- התשובות שלך ---")
    for category, answer in answers.items():
        print(f"{category}: {answer}")

if __name__ == "__main__":
    play_game()