import random


def play():
    expected_word = random.choice(words)
    hidden_word = list("-" * len(expected_word))

    attempts = 8
    uncovered_letters = set(expected_word)
    provided_letters = set()
    valid_letters = "abcdefghijklmnopqrstuvwxyz"

    while attempts != 0 and len(uncovered_letters) != 0:
        print()
        print("".join(hidden_word))
        letter = input("Input a letter: ")
        if letter in provided_letters:  # Czemu w Pythonie, do cholery, nie ma switcha/when?
            print("You've already guessed this letter.")
        elif len(letter) != 1:
            print("Please, input a single letter.")
        elif letter not in valid_letters:
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in uncovered_letters:
            provided_letters.add(letter)
            uncovered_letters.remove(letter)
            for i in range(len(expected_word)):
                if expected_word[i] == letter:
                    hidden_word[i] = letter
        else:
            provided_letters.add(letter)
            print("That letter doesn't appear in the word.")
            attempts -= 1

    print()

    if len(uncovered_letters) == 0:
        print(f"You guessed the word {expected_word}!")
        print("You survived!")
        return True
    else:
        print("You lost!")
        return False


print("H A N G M A N")
words = ["python", "java", "swift", "javascript"]
won_times = 0
lost_times = 0
while True:
    action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if action == "exit":
        break
    if action == "play":
        result = play()
        if result:
            won_times += 1
        else:
            lost_times += 1
    if action == "results":
        print(f"You won: {won_times} times")
        print(f"You lost: {lost_times} times")
