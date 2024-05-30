from textblob import TextBlob
import random
import sys
import time

def get_sentiment(sentence):
    blob = TextBlob(sentence)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "good and positive"
    elif sentiment_score < 0:
        return "bad and/or negative"
    else:
        return "unreadable! retry;"

# First interaction with nnt == "bad and/or negative":
# print(f"AI interpreted your feeling as: {setiment}")

name = str(input("I'm Kristy, what's your name? "))

while True:
    user_input = input(f"Hello {name}, how are you?  ")

    sentiment = get_sentiment(user_input)
    if sentiment == "good and positive":
        print(f"AI interpreted your feeling as: {sentiment}")
        break
    if sentiment == "bad and/or negative":
        print(f"AI interpreted your feeling as: {sentiment}")

        bad_reasons = ["anxiety", "stress", "trauma", "depression", "illness"]
        why_bad = input("Why do you feel bad? ")
        if why_bad.lower() in bad_reasons:
            print(f"Help for '{why_bad}' can be found here: https://anacy.netlify.app")
            break
        elif why_bad.lower() not in bad_reasons:
            print(f"Your problem '{why_bad}' is not understandable for me. Please retry: ")
            continue

def askos():
    while True:
        options = ["scissors", "rock", "paper"]
        bot_choice = random.choice(options)
        print(f"Bot: {bot_choice}")
        user_choice = input("Choose scissors, rock, or paper: ").lower()

        if user_choice not in options:
            print("Invalid choice!")
            continue

        if user_choice == bot_choice:
            print("Draw")
        elif (user_choice == "scissors" and bot_choice == "rock") or \
                (user_choice == "rock" and bot_choice == "paper") or \
                (user_choice == "paper" and bot_choice == "scissors"):
            print("You lost")
        else:
            print("You won!")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print(f"Sorry you chose {play_again}. Bye bye")
            break

def secondInteraction():
    ask_game = str(input("Do you want to play a game? "))
    yes_words = ["yes", "yeah", "positive", "ok", "okay"]
    no_words = ["no", "don't", "nah", "negative"]

    while True:
        try:
            if ask_game.lower() in yes_words:
                askos()
                break
            elif ask_game.lower() in no_words:
                print("Okay, bye bye") and sys.exit()
                break
        except ValueError:
            print("VALUEERROR")

secondInteraction()

