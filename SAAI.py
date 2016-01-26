while True:
    userInput = raw_input(">>> ").lower()
    if userInput in ['hi', 'hello']:
        print("Hello")
        os.system("say 'hello'")
    else:
        print("I did not understand what you said")
