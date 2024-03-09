questions = [
    {
        "Question": "What is the capital of Armenia: ",
        "Answer": "yerevan",
        "XP": 10
    },
    {
        "Question": "11 + 11: ",
        "Answer": "22",
        "XP": 10
    },
    {
        "Question": "cos 60°= : ",
        "Answer": "1/2",
        "XP": 10
    },
    {
        "Question": "The biggest country: ",
        "Answer": "russia",
        "XP": 10
    },
    {
        "Question": "Who is the first person in the world?: ",
        "Answer": "adam",
        "XP": 10
    },
    {
        "Question": "Who is the father of mechanics?: ",
        "Answer": "isaac newton",
        "XP": 15
    },
    {
        "Question": "who is the richest man in the world?: ",
        "Answer": "elon musk",
        "XP": 15
    },
    {
        "Question": "Who Is the Oldest God of This World?: ",
        "Answer": "anu",
        "XP": 15
    },
    {
        "Question": "what is the oldest religion?: ",
        "Answer": "hindu",
        "XP": 15
    },
    {
        "Question": "who is lewandowski grandfather?: ",
        "Answer": "bogdan Lewandowski",
        "XP": 15
    },
    {
        "Question": "The most popular name in the world: ",
        "Answer": "maria",
        "XP": 20
    },
    {
        "Question": "who is the father of mathematics?: ",
        "Answer": "archimedes",
        "XP": 20
    },
    {
        "Question": "Which country is home to the Eiffel Tower?: ",
        "Answer": "france",
        "XP": 20
    },
    {
        "Question": "What is the capital of Denmark?: ",
        "Answer": "copenhagen",
        "XP": 20
    },
    {
        "Question": "What is the name of the supercontinent that existed 200 million years ago?: ",
        "Answer": "pangea",
        "XP": 20
    },
    {
        "Question": "Which country are the Great Pyramids of Giza located in?: ",
        "Answer": "egypt",
        "XP": 25
    },
    {
        "Question": "Ljubljana is the capital of which country?: ",
        "Answer": "slovenia",
        "XP": 25
    },
    {
        "Question": "What do you call land with water on three sides?: ",
        "Answer": "peninsula",
        "XP": 25
    },
    {
        "Question": "Which country has the most volcanoes?: ",
        "Answer": "indonesia ",
        "XP": 25
    },
    {
        "Question": "Name the U.S. state that’s home to no documented poisonous snakes?: ",
        "Answer": "alaska",
        "XP": 25
    },
]

import random


def get_content(filename):
    f = open(filename)
    return f.read()


def get_lines(filename):
    f = open(filename)
    return f.readlines()


def ask_question():
    random_question = random.choice(questions)
    random_key = random_question["Question"]
    print("Question: ", random_key)
    answer = input("Answer:  ")
    return random_question, answer.lower()


def update_xp(xp, earned_xp):
    xp += earned_xp
    print(True)
    print(xp, "XP")
    return xp


def calculate_level(xp):
    if xp == 0:
        return " 0"
    elif 0 < xp <= 25:
        return " 1"
    elif 26 <= xp <= 50:
        return " 2"
    elif 51 <= xp <= 100:
        return " 3"
    elif 101 <= xp <= 150:
        return " 4"
    elif 151 <= xp <= 200:
        return " 5"
    elif 201 <= xp <= 250:
        return " 6"


def record_players(name, xp):
    with open("top.txt", "a") as f:
        f.write(f"{name} {xp}\n")


def sort_players():
    with open("top.txt", "r") as f:
        players = f.readlines()
    players.sort(key=lambda x: int(x.split()[1]), reverse=True)
    with open("top.txt", "w") as f:
        for player in players:
            f.write(player)


name = input('Enter your name: ')
print('Welcome', name)
print()


def play_game():
    xp = 0
    count = 0
    while count != 11:
        count += 1
        question, answer = ask_question()
        if answer == question["Answer"]:
            xp = update_xp(xp, question["XP"])
        else:
            player_lvl = calculate_level(xp)
            print(f"You gathered {xp}XP")
            print(f"Your level is {player_lvl}")
            record_players(name, xp)
            return
        player_lvl = calculate_level(xp)
        print(player_lvl)

    print(f"You gathered {xp}XP")
    record_players(name, xp)


play_game()
sort_players()
