#Import Modules
import pyttsx
from random import randint
import datetime
from chatterbot import ChatBot
import yweather

#Variables and commands
engine = pyttsx.init()
client = yweather.Client()

bot = ChatBot("No Output",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
    io_adapter="chatterbot.adapters.io.NoOutputAdapter",
    database="./database.db")

bot = ChatBot("SAAI")

#age since launch
now = datetime.datetime.now()
birthdate = datetime.datetime(2016, 01, 26, 11, 37, 00)
age = now - birthdate


class choice:
    def __init__(self, data):
        self.data = data
    def call(self):
        random = randint(1, len(data))
        return data[random - 1]


while True:

    userInput = raw_input(">>> ").lower()
    userInput = ''.join([c for c in userInput if c not in ('!', '?', '.', ',')])
    print ""

    if "buggy" in userInput or "bug" in userInput:
        print "Please visit my GITHUB page to report bugs or request features."
        print "You will find my page at: github.com/Cyber-Shadow/SAAI)"
        engine.say("Please visit my GITHUB page to report bugs or request features..."
                   " ... You will find my page at: github.com/Cyber-Shadow/SAAI")
        engine.runAndWait()
    elif "weather" in userInput:
        weathersyd = client.fetch_weather("1105779", metric=True)
        w1 = weathersyd["condition"]["text"]
        w2 = weathersyd["condition"]["temp"]

        print ("It's currently " + w1 + " and is " + w2 + " degree celsius. ")
        engine.say ("It's currently" + w1 + " and is " + w2 + "degree celsius. ")
        engine.runAndWait()

    elif userInput in ['hi saai', 'hello saai']:
        data = ["Hello to you too.", "You know my name!"]
        x = choice(data)
        print(x.call())
    elif userInput in ['tell me a joke', "tell me something funny"]:
        data = ["NO", "What do you call a blonde who has dyed her hair brown? ... Artificial intelligence!",
                "I had to sell my first vacuum cleaner ... It sucked.",
                "Why did the platypus cross the road? ... Because it was in the wrong joke.",
                "How does the d cut his hair? ... Eclipse it."]
        x = choice(data)
        print(x.call())
    elif userInput in ['what is your age', 'how old are you']:
        print ("I am " + str(age) + "old, since you launched me")
        engine.say("I am")
        engine.say(age)
        engine.say("old, since you launched me")
        engine.runAndWait()
    else:
        botoutput = bot.get_response(userInput)
        bot.train("chatterbot.corpus.english.conversations")
        engine.say(botoutput)
        engine.runAndWait()

