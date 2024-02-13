#!/usr/bin/env python
# coding: utf-8

# # HANGMAN GAME


english_words = [
    "adventure",
    "mystery",
    "journey",
    "courageous",
    "freedom",
    "discover",
    "brilliant",
    "treasure",
    "victory",
    "curious",
    "discover",
    "history",
    "explore",
    "imagine",
    "clever",
    "peaceful",
    "harmony",
    "challenge",
    "balance",
    "harmony"
]

HangMan = ['''
    +---+
        |
        |
        |
        |
        |
    ========''','''
    +---+
    |   |
        |
        |
        |
        |
    ========''','''
    +---+
    |   |
    o   |
        |
        |
        |
    ========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
    ========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
    ========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
    ========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
    ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
    ========'''
]

import random

random_word = random.choice(english_words).upper()

# print("Random word:", random_word)

HangMan_Count = 0
count = 0

strs = ['_' for _ in range(len(random_word))]

while True:
    while HangMan_Count != (len(HangMan) - 1):
        input_word = input("\nEnter your guess: ").upper()
        for item in range(len(random_word)):
            if random_word[item] == input_word:
                strs[item] = input_word
        if input_word in strs:
            print("\n")
            print(" ".join(strs))
            print("\nCORRECT")
            print(HangMan[HangMan_Count])
            print(f"\nChance left: {len(HangMan) - (count + 1)}")
        else:
            if HangMan_Count == len(HangMan):
                break
            HangMan_Count += 1
            count += 1
            print("\n")
            print(" ".join(strs))
            print("\nWRONG")
            print(HangMan[HangMan_Count])
            print(f"\nChance left: {len(HangMan) - (count + 1)}")
        if '_' not in strs:
            break


    if '_' not in strs:
        print(f"\nYOU 'WON' >> The correct word is {random_word}")
    else:
        print(f"\nYOU 'LOST' >> The correct word is {random_word}")

    condition = input("Play Again? >> Type 'yes' or 'no': ")
    if condition == 'no':
        print("GAME ENDED")
        break
    elif condition == 'yes':
        # Reset variables for a new game
        HangMan_Count = 0
        count = 0
        random_word = random.choice(english_words).upper()
        strs = ['_' for _ in range(len(random_word))]
        continue
