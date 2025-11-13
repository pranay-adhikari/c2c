# Scenario: A delivery app support chatbot for when someone's having issues with their order/their order hasn't arrived as expected
import re
import random
from order import Order

def welcome_user():
    print("\nHi there! Sorry your delivery hasn't arrived as expected; let's get this sorted.")

def display_menu():
    while True:
        print('-----------------------------------------')
        user_choice = input(f'Please choose from the following options:\n'
        '1) Estimated time of arrival\n2) Request delay reason\n3) Resolution options\n4) Connect with human support\n5) Exit the conversation\n\n')
        print()
        if re.match('^[1-5]$', user_choice):
            return int(user_choice)
        else: 
            print('Please enter a choice from 1-5.')

def handle_user_choice(user_choice, account):
    order = account["current_order"]
    is_premium = account["premium"]
    match user_choice:
        case 1:
            print(Order.get_ETA(order))
        case 2:
            print(Order.get_delay_reason(order))
        case 3:
            print(Order.get_resolution_options(order, is_premium))
            print('We hope you are satisfied with the outcome!')
        case 4:
            print(Order.human_support(order))
        case 5:
            return False
    return True

def menu_loop(account):
    running = True
    while running:
        user_choice = display_menu()
        running = handle_user_choice(user_choice, account)

def simulate_customer_account():
    subscribed_to_premium = random.randint(0, 1) == 1
    order = Order()
    return {"current_order":order, "premium":subscribed_to_premium}

def main():
    welcome_user()
    menu_loop(simulate_customer_account())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('Goodbye')