import pyttsx
engine = pyttsx.init()
while True:
    userInput = raw_input(">>> ").lower()
    if userInput in ['hi', 'hello']:
        print("Hello")
        engine.say("hello")
        engine.runAndWait()

    else:
        print("I did not understand what you said")
