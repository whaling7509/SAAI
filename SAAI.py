import pyttsx
from random import randint

engine = pyttsx.init()

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
        choice("Hello!", "Hi there!")
    elif userInput in ['hi saai', 'hello saai']:
        choice("Hello to you too.", "You know my name!")
    elif userInput in ['tell me a joke', "tell me something funny"]:
        choice5("NO", "What do you call a blonde who has dyed her hair brown? ... Artificial intelligence!",
                "I had to sell my first vacuum cleaner ... It sucked.",
                "Why did the platypus cross the road? ... Because it was in the wrong joke.",
                "How does the moon cut his hair? ... Eclipse it." )
    else:
        print("I don't understand.")
        engine.say("I don't understand.")
        engine.runAndWait()

