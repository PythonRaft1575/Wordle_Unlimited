import nltk, random, os, time
nltk.download("words")
from nltk.corpus import words

optional_words = words.words()

os.system("clear")

words = []
while True:
  print("\033[1;32mW\033[1;33mo\033[1;37mr\033[1;32md\033[33ml\033[1;37me\033[0m  BY ROGFE2\n")
  length = int(input("Length: "))
  os.system("clear")
  break

for word in optional_words:
  if len(word) == length:
    words.append(word)

word = random.choice(words)
guessed_words = []
while True:
  print("\033[1;32mW\033[1;33mo\033[1;37mr\033[1;32md\033[33ml\033[1;37me\033[0m  BY ROGFE2\n")
  if len(guessed_words) == 6:
    while True:
      print(f"The word was {word}")
      time.sleep(1)
      os.system("clear")
  elif len(guessed_words) == 0:
    pass
  else:
    for guessed_word in guessed_words:
      letters_checked = []
      for i in range(5):
        if guessed_word[i] == word[i]:
          letters_checked.append(guessed_word[i])
          print(f"\033[32m{guessed_word[i]}\033[0m", end = "")
        elif guessed_word[i] in word and guessed_word[i] not in letters_checked:
          print(f"\033[33m{guessed_word[i]}\033[0m", end = "")
          letters_checked.append(guessed_word[i])
        else:
          print(guessed_word[i], end = "")
      print()
    print()
  guess = input("Guess: ")
  time.sleep(1)
  os.system("clear")
  if guess not in words:
    print("Not in word list!")
    time.sleep(1)
    os.system("clear")
    continue
  elif guess in guessed_words:
    print("Already guessed!")
    time.sleep(1)
    os.system("clear")
  elif len(guess) != length:
    print(f"Must be {length} letter(s) long")
    time.sleep(1)
    os.system("clear")
  else:
    guessed_words.append(guess)
  if guess == word:
    print("You got it! Well done!")
    break