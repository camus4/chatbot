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
        return "bad and / or negative"
    else:
        return "unreadable! retry;  "

# First interaction with nnt == "bad and / or negative":
        print(f"AI interpreteed your feeling as: {setiment}")

name = str(input("im kristy, whats your name? "))

while True:
    user_input = input(f"hello {name}, how are you?  ")

    setiment = get_sentiment(user_input)
    if setiment == "good and positive":
        print(f"AI interpreted your feeling as: {setiment}")
        break
    if setiment == "bad and / or negative":
        print(f"AI interpreteed your feeling as: {setiment}")

        bad_reasons = ["Anxiety", "stress", "trauma", "depression", "illness"]
        why_bad = input("why do you feel bad? ")
        if why_bad.lower() in bad_reasons:
            print(f"help for ' {why_bad} ' can you find here: https://anacy.netlify.app")
            break
        elif why_bad.lower() not in bad_reasons:
            print(f"your problem ' {why_bad} ' is not understandable for me. please retry: ")
            continue


def askos():


    while True:
        options = ["schere", "stein", "papier"]
        bot_choice = random.choice(options)
        print(f"Bot: {bot_choice}")
        user_choice = input("Wähle Schere, Stein oder Papier: ").lower()

        if user_choice not in options:
            print("invalue! ")
            continue

        if user_choice == bot_choice:
            print("Unentschieden")
        elif (user_choice == "schere" and bot_choice == "stein") or \
                (user_choice == "stein" and bot_choice == "papier") or \
                (user_choice == "papier" and bot_choice == "schere"):
            print("Du hast verloren")
        else:
            print("Du hast gewonnen!")

        play_again = input("Möchtest du noch einmal spielen? (ja/nein): ").lower()

        if play_again != "ja":
            print(f"schade das du dich für {play_again} entschieden hast. bye bye")
            break


def secondInteraction():
    ask_game = str(input("do you want to play a game? "))
    yes_words = ["yes", "yeah", "positive", "ok", "okay"]
    no_words = ["no", "dont", "nah", "negative"]

    while True:
        try:
            if ask_game.lower() in yes_words:
                askos()
                break
            elif ask_game.lower() in no_words:
                print("okay bye bye") and sys.exit()
                break
            # sec interarom textblob import TextBlob
        except ValueError:
            print("VALUEERROR")


secondInteraction()

