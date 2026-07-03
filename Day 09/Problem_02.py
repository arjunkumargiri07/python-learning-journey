import random

def game():
    print("You are playing a game")
    score = random.randint(1, 100)

    try:
        with open("hiscore.txt", "r") as f:
            data = f.read().strip()
            if data != "":
                hiscore = int(data)
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0

    print("Your score is:", score)
    print("High Score:", hiscore)

    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("🎉 Congratulations! You have the highest score!")

    return score

game()