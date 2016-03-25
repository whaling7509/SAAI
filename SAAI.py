# Import Modules
import pyttsx
from random import randint
import datetime
from chatterbot import ChatBot
import yweather
import string
import speech_recognition as sr
import threading

# Variables and commands
engine = pyttsx.init()
client = yweather.Client()
stuff = ""
botlearn = 1

bot = ChatBot("No Output",
              storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
              logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
              io_adapter="chatterbot.adapters.io.NoOutputAdapter",
              database="./database.db")

bot = ChatBot("SAAI")

# age since launch
now = datetime.datetime.now()
birthdate = datetime.datetime(2016, 01, 26, 11, 37, 00)
age = str(now - birthdate)
agelist = [str(str(age[::-1])[16:])[::-1], str(str(age[::-1])[13:15])[::-1], str(str(age[::-1])[10:12])[::-1],
           str(str(age[::-1])[7:9])[::-1], str(str(age[::-1])[:6])[::-1]]
age = str(agelist[0] + " " + agelist[1] + " hours, " + agelist[2] + " minutes, " + agelist[3] + " seconds, " + agelist[
    4] + " microseconds ")

# maths notation
mathsnotation = ["+", "-", "*", "/", "^", "%"]


class choice:
    def __init__(self, data):
        self.data = data

    def call(self):
        random = randint(1, len(data))
        return data[random - 1]


def checkthing(a):
    for i in mathsnotation:
        if i in a:
            return True
    return False


def talk(string):
    print(string)
    engine.say(string)


def mainloop():
    global botlearn, srcheck, userInput
    print ""
    userInput = raw_input(">>> ").lower()
    userInput = ''.join([c for c in userInput if c not in ('!', '?', '.', ',')])
    print ""
    ifwhat()

def ifwhat():
    global botlearn
    if "buggy" in userInput or "bug" in userInput:
        talk("Please visit my GITHUB page to report bugs or request features. "
             "You will find my page at: github.com/Cyber-Shadow/SAAI")
        engine.runAndWait()
    elif "weather" in userInput:
        weathersyd = client.fetch_weather("1105779", metric=True)
        w1 = weathersyd["condition"]["text"]
        w2 = weathersyd["condition"]["temp"]

        talk("It's currently " + w1 + " and is " + w2 + " degrees Celsius.")
        engine.runAndWait()

    elif userInput in ['hi saai', 'hello saai']:
        data = ["Hello to you too.", "You know my name!"]
        x = choice(data)
        talk(x.call())
    elif userInput in ['tell me a joke', "tell me something funny"]:
        data = ["NO", "What do you call a blonde who has dyed her hair brown? ... Artificial intelligence!",
                "I had to sell my first vacuum cleaner ... It sucked.",
                "Why did the platypus cross the road? ... Because it was in the wrong joke.",
                "How does the moon cut his hair? ... Eclipse it."]
        x = choice(data)
        talk(x.call())
    elif userInput in ['what is your age', 'how old are you']:
        talk("I am " + str(age) + "old, since you launched me")
        engine.runAndWait()
    elif checkthing(userInput):
        print(
        "The answer is" + str((eval((userInput.translate(None, string.ascii_letters).translate(None, " "))))) + ".")
    elif "python 3" in userInput:
        talk("Do not talk about that useless language to me!")
    elif "im " in userInput:
        stuff = " " + userInput[3:]
        talk("Hi, " + userInput[3:] + "! I'm SAAI!")
    elif "whats the time" in userInput or "what is the time" in userInput:
        talk("Time to get a watch" + stuff + ".")
    elif "developer1:502" in userInput:
        if botlearn == 0:
            botlearn = 1
            print "botlearn = 1"
        elif botlearn == 1:
            botlearn = 0
            print "botlearn = 0"
    elif "developerinfo:502" in userInput:
        print "botlearn = " + str(botlearn)
    else:
        botoutput = bot.get_response(userInput)
        if botlearn == 1:
            bot.train("chatterbot.corpus.english.conversations")
        engine.say(botoutput)
        engine.runAndWait()


r = sr.Recognizer()
m = sr.Microphone()


def voicerec():
    global srcheck, userInput
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
        with m as source:
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            if str is bytes:
                userInput = (value)
                print ""
                print ">>> " + userInput
                ifwhat()
        except sr.UnknownValueError:
            print ""
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


thread = threading.Thread(target=mainloop)
thread.start()
otherThread = threading.Thread(target=voicerec)
otherThread.start()
