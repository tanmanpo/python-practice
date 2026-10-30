vowels = {"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o"}

text = "あいう"

for letter in text:
    print(vowels[letter], end="")
