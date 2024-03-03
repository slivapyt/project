import random
answers = []
count = 0


def trans_morze(word):
    """Переводит на морзе"""
    morze = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    morze_word = []
    for letter in word:
        morze_word.append(morze[letter])
    return morze_word


def random_word():
    words = ["day", "sun", "rice", "snow", "rain", "war", "lizard", "fix"]
    random_result = random.choice(words)
    return random_result


def result_answers(answers):
    true_ans = 0
    false_ans = 0
    for answer in answers:
        if answer is True:
            true_ans += 1
        else:
            false_ans += 1
    print(f"""
Всего задачек: {len(answers)}
Отвечено верно: {true_ans}
Отвечено неверно: {false_ans} """)


input("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем
""")

while count < 5:
    r_w = random_word()
    r_morze_w = (trans_morze(r_w))
    response = input(''.join(r_morze_w))
    if response == r_w:
        count += 1
        print(f"Верно, {r_w} \n")
        answers.append(True)
    else:
        count += 1

        print(f"Неверно {r_w}\n")
        answers.append(False)
result_answers(answers)
from get_word import BasicWord
from player import Player
from utils import load_web_dictionary
random_word = load_web_dictionary()
get_rand_word = BasicWord(random_word)


name = input("Введите имя игрока\n")

print(f"Привет, {name}!")
print(f"Составьте {get_rand_word.quantity_short_words()} слов из слова {
      get_rand_word.get_main_word().upper()}\nСлова должны быть не короче 3 букв")
print(f'Что бы закончить игру, угадайте все слова или напишите "стоп"')
print(f"Поехали, ваше первое слово?\n")

player_class = Player(name)

while player_class.get_quantity_words() < get_rand_word.quantity_short_words():
    inp_word = input()
    if len(inp_word) > 2:
        if inp_word != "стоп":
            if get_rand_word.try_chek(inp_word):
                if not player_class.check_word_in_used(inp_word):
                    print("верно")
                    player_class.get_used_words(inp_word)
                else:
                    print("уже использовано")
            else:import requests
# import json
from random import choice


def load_web_dictionary():
    '''Получаем данные о студенте из json'''
    web_words = "https://www.jsonkeeper.com/b/ETPW"
    web_4len = requests.get(web_words)
    data = web_4len.json()
    return choice(data)

                print("неверно")
        else:
            break
    else:
        print("слишком короткое слово")

print(f"Игра завершена, вы угадали {
    player_class.get_quantity_words()} слов!")
