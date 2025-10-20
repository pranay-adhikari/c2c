import re
import random
import order

menu_loop_running = True

def welcome_user():
    print("Hi there! Sorry your delivery hasn't arrived as expected; let's get this sorted.")

def display_menu():
    while True:
        user_choice = input(f'Hi, please choose from the following options:\n'
        '1. Check delivery status\n2. Request delay reason\n3. Estimated time of arrival\n4. Resolution options\n5. Connect with human support\n6. Exit the conversation\n\n')
        print()
        if re.match('^[1-6]$', user_choice):
            return int(user_choice)
        else: 
            print('Please enter an integer from 1-6.')

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
            pass
        case 6:
            global menu_loop_running
            menu_loop_running = False

def menu_loop():
    while menu_loop_running:
        user_choice = display_menu()
        handle_user_choice(user_choice)

def simulate_customer_account():
    past_orders = []
    subscribed_to_premium = False
    for i in range(5):
        order_ID = random.randint(100000, 999999) # Fix this to make sure every order ID is unique
        past_orders.append(order(order_ID))
    if random.randint(1, 10) <= 5:
        subscribed_to_premium = True
    return [past_orders, subscribed_to_premium]

def start():
    welcome_user()
    menu_loop()

if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as e:
        print ('Goodbye')