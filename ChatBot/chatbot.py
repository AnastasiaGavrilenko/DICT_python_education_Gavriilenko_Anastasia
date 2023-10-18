# chatbot.py
import datetime

bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

print("Please, remind me your name.")
user_name = input("> Alex ")

print(f"What a great name you have, Alex {user_name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5, and 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))

for i in range(number + 1):
    print(f"{i} !")

print("Completed, have a nice day!")