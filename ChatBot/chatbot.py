# chatbot.py
import datetime

bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

print("Please, remind me your name.")
user_name = input("> Alex ")

print(f"What a great name you have, Alex {user_name}!")