import random
class Order:
    def __init__(self):
        self.status = random.randint(1, 10)
        self.ETA = random.randint(10, 45)
        self.price = round(random.uniform(10, 100), 2)
        self.credits = random.randint(0, 5000)
        self.phone_number = f'{random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}'
        self.is_resolved = False

    def get_ETA(self):
        return f"Your estimated time of arrival is {self.ETA}{' minutes' if self.ETA != 'NA' else ''}\n"

    def get_delay_reason(self):
        match self.status:
            case 1:
                return 'Your driver is stuck in traffic\n'
            case 2:
                return 'Your driver is waiting for your order to be completed\n'
            case 3:
                return 'Your driver is driving to you\n'
            case 4:
                self.status = random.randint(1, 10)
                return 'Unable to determine a delay reason; please try again shortly\n'
            
            case _:
                self.ETA = "NA"
                return 'Your driver is not able to make it. We can offer a full refund or equivalent credits in the \'Resolution options\' tab\n'
    
    def get_resolution_options(self, is_premium):
        new_balance = (self.price * 100 + self.credits) * 1.25 if is_premium else self.price * 100 + self.credits
        to_be_added = new_balance - self.credits
        if self.status > 4 and not self.is_resolved:
            while True:
                choice = input(
                    f"Please choose from the following options:\n"
                    f"1) ${self.price} refund\n"
                    f"2) {to_be_added} credits"
                    f"{' (includes a 1.25x bonus for premium subscription!)' if is_premium else ''}\n"
                )
                if choice == '1' or choice == '2':
                    break
                else:
                    print("Not a valid option")
            
            
            self.is_resolved = True
            if choice == '1':
                return f'\n${self.price} will be refunded to you within 2-4 business days'
            else:
                return f'\n{to_be_added} credits were successfully added to your account\nNew Balance: {new_balance}'
        else:
            return 'Your order has been reimbursed' if self.is_resolved else 'You currently do not qualify for resolution options'
    
    def human_support(self):
        return f'Please call \'{self.phone_number}\' to address any concerns over your order'