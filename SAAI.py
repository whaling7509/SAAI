#Import Modules
import pyttsx
from random import randint
import datetime

#Variables
engine = pyttsx.init()

now = datetime.datetime.now()

birthdate = datetime.datetime(2016, 01, 26, 11, 37, 00)
age = now - birthdate

def choice2(str, str2):
    random = randint(1, 2)
    if random == 1:
        print(str)
        engine.say(str)
        engine.runAndWait()
    else:
        print(str2)
        engine.say(str2)
        engine.runAndWait()
    
    
def choice5(str, str2, str3, str4, str5):
    random = randint(1, 5)
    if random == 1:
        print(str)
        engine.say(str)
        engine.runAndWait()
    elif random == 2:
        print(str2)
        engine.say(str2)
        engine.runAndWait()
    elif random == 3:
        print(str3)
        engine.say(str3)
        engine.runAndWait()
    elif random == 4:
        print(str4)
        engine.say(str4)
        engine.runAndWait()
    else:
        print(str5)
        engine.say(str5)
        engine.runAndWait()

while True:
    userInput = raw_input(">>> ").lower()
    userInput = ''.join([c for c in userInput if c not in ('!', '?', '.', ',')])
    if userInput in ['hi', 'hello']:
        choice2("Hello!", "Hi there!")
    elif userInput in ['hi saai', 'hello saai']:
        choice2("Hello to you too.", "You know my name!")
    elif userInput in ['tell me a joke', "tell me something funny"]:
        choice5("NO", "What do you call a blonde who has dyed her hair brown? ... Artificial intelligence!",
                "I had to sell my first vacuum cleaner ... It sucked.",
                "Why did the platypus cross the road? ... Because it was in the wrong joke.",
                "How does the moon cut his hair? ... Eclipse it." )
    elif userInput in ['age']:
        print (age)
        engine.say("I am")
        engine.say(age)
        engine.say("old")
        engine.runAndWait()
    else:
        print("I don't understand.")
        engine.say("I don't understand.")
        engine.runAndWait()
