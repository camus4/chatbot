
import sys
import time
import random

def for_loop():
    end_orakel = random.randint(0, 10)
    for i in range(end_orakel):
        time.sleep(0.35)
        print(i)
def first_round():

    def ask_nextRound():

        print(f"dein guthaben: {guthaben} ")
        einsatz_2 = int(input("neuer einsatz: "))

        for_loop()
        if einsatz_2 < end_orakel:
            print(f"gewonnen! dein guthaben: {guthaben * einsatz_2}")

        if einsatz_2 >= end_orakel:
            neues_guthaben = guthaben -einsatz_2
            print(f"verloren! dein guthaben: {neues_guthaben}")
            print(f"NEUES GUTHABEN: {guthaben - einsatz_2}")

    guthaben = int(input("guthaben: "))
    einsatz = int(input("einatz: "))

    end_orakel = random.randint(0, 10)
    for i in range(end_orakel):
        time.sleep(0.35)
        print(i)

    if einsatz < end_orakel:
        print(f"gewonnen! guthaben: {guthaben * einsatz}")
        guthaben = guthaben * einsatz
        ask = input("willst du die nächste runde spielen? j für ja und n für nein: ")
        if ask.lower() == "j":

            print("Nächste runde...")
            ask_nextRound()

    elif einsatz >= 0:
        print(f"verloren! guthaben: {guthaben - einsatz}")
        guthaben = guthaben - einsatz
        if guthaben <= 0:
            print("tschau! ")
            sys.exit()

first_round()