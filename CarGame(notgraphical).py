command = ""
while command.lower() != "quit":
    command = input(">")
    if command.lower() == "start":
        print("Car started...")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "help":
        print("Available commands: start, stop, quit")
    elif command == "quit":
        break
    else:
        print("Invalid command.")