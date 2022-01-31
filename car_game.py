from tracemalloc import start


command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start" and not started:
        print("the car started")
        started = True

    elif command == "start" and started:
        print("The car is already started")

    elif command == "stop" and started:
        print("the car stopped")
        started = False

    elif command == "stop" and not started:
        print("the car is already stop")

    elif command == "help":
        print('''
start - to start
stop - to stop
quit - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand")

    

