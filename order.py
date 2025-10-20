import random
class order:
    def __init__(self, order_ID):
        self.order_ID = order_ID
        self.status = random.randint(1, 3)

    def get_delay_reason(self):
        match self.status:
            case 1:
                return 'Your driver is stuck in traffic'
            case 2:
                return 'Your driver is waiting for your order to be completed'
            case 3:
                return 'Your driver is not able to make it. We can offer a full refund or credits'
    
    def get_ETA(self):
        match self.status:
            case 1:
                return f'{random.randint(10, 25)}'
            case 2:
                return f'{random.randint(30, 60)}'
            case 3:
                return 'N/A'