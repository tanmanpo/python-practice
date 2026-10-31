import random

kana = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
}

score = 0
rounds = 5

for i in range(rounds):
    letter = random.choice(list(kana))
    answer = input(f"{i + 1}. How do you read {letter}? ").strip().lower()

    if answer == kana[letter]:
        print("Correct!")
        score += 1
    else:
        print("Nope, it's", kana[letter])

print(f"Score: {score}/{rounds}")
