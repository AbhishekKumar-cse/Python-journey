command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car start ...")
    elif command == "stop":
        if not started:   
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped...")
    elif command.lower() == "help":
        print("Available commands: start, stop, quit")
    elif command == "quit":
        break
    else:
        print("Invalid command.")