# Scenario: A delivery app support chatbot for when someone's having issues with their order/their order hasn't arrived as expected
import re
import random
from order import Order

def display_menu():
    while True:
        print('-----------------------------------------')
        user_choice = input(f'Please choose from the following options:\n'
        '1) Estimated time of arrival\n2) Request delay reason\n3) Resolution options\n4) Connect with human support\n5) Exit the conversation\n\n').strip()
        print()
        if re.match('^[1-5]$', user_choice):
            return int(user_choice)
        else: 
            print('Please enter a choice from 1-5.')

def handle_user_choice(user_choice, account):
    order = account["current_order"]
    is_premium = account["premium"]
    name = account["name"]
    age = account["age"]

    match user_choice:
        case 1:
            print(Order.get_ETA(order))
        case 2:
            print(Order.get_delay_reason(order))
        case 3:
            print(Order.get_resolution_options(order, is_premium))
            print('We hope you are satisfied with the outcome!')
        case 4:
            print(Order.human_support(order, age, name))
        case 5:
            print(f'Thank you for using the delivery support chatbot. Goodbye!')
            return False
    return True

def menu_loop(account):
    running = True
    while running:
        user_choice = display_menu()
        running = handle_user_choice(user_choice, account)

# Creates the user account with a chance for premium
def simulate_customer_account():
    print("\nHi there! Sorry your delivery hasn't arrived as expected; let's get this sorted.")
    name = input('What is your name?: ').strip()
    while True:
        age = input('What is your age?: ').strip()
        if age.isdigit():
            age = int(age)
            break
        else:
            print('Not a valid age')

    print(f'\nThanks {name}! I\'ll help you right away.')
    subscribed_to_premium = random.randint(0, 1) == 1
    order = Order()
    return {"current_order":order, "premium":subscribed_to_premium, "name":name, "age":age}

def main():
    menu_loop(simulate_customer_account())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('Goodbye')