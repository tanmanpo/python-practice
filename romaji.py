kana = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
     "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
}

text = "あいう"

for letter in text:
    print(kana[letter], end="")
