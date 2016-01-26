import pyttsx
from random import randint

engine = pyttsx.init()

def choice(str, str2):
    random = randint(1, 2)
    if random == 1:
        print(str)
        engine.say(str)
        engine.runAndWait()
    else:
        print(str2)
        engine.say(str2)
        engine.runAndWait()

while True:
    userInput = raw_input(">>> ").lower()
    if userInput in ['hi', 'hello']:
        choice("Hello!", "Hi there!")
    elif userInput in ['hi saai', 'hello saai']:
        choice("Hello to you too.", "You know my name!")
    else:
        print("I don't understand.")
        engine.say("I don't understand.")
        engine.runAndWait()

