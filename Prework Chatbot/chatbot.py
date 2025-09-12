import re

menu_loop_running = True

def welcome_user():
    print("Welcome to the Elite 101 Chatbot!")
    name = input("What is your name?: ")
    age = input("What is your age?: ")
    return [name, age]

def display_menu(name):
    while True:
        user_choice = input(f"Hi {name}, please choose from the following options:\n" \
        "1. Option 1\n2. Option 2\n3. Option 3\n4. Option 4\n5. Exit the conversation\n\n")
        print()
        if re.match("^[1-5]$", user_choice):
            return int(user_choice)
        else: 
            print("Please enter an integer from 1-5.")

def handle_user_choice(user_choice):
    match user_choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            global menu_loop_running
            menu_loop_running = False

def menu_loop(name):
    while menu_loop_running:
        user_choice = display_menu(name)
        handle_user_choice(user_choice)

def start():
    user_data = welcome_user()
    name = user_data[0]
    age = user_data[1]
    menu_loop(name)
    print(f"Goodbye, {age} year old {name}.")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt as e:
        print ("Goodbye")