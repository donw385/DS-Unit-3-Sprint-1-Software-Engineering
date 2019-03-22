class Product(object):
    """
    A Python Class from which Acme Co. can build specific product instances
    """
    import random
    Prod_ID = random.randint(1000000, 9999999)
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=Prod_ID):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability
        self.identifier=identifier

    def stealability(self):
        ratio = (self.price)/(self.weight)
        message = ["Not so stealable...", "Kinda stealable.", "Very stealable!"]
        if(ratio < 0.5):
            return message[0]
        elif(0.5 <= ratio and ratio < 1.0):
            return message[1]
        else:
            return message[2]

    def explode(self):
        ratio_2 = (self.flammability)*(self.weight)
        message_2 = ["...fizzle", "...boom!", "...BABOOM!"]
        if(ratio_2 < 10):
            return message_2[0]
        elif(10 <= ratio_2 and ratio_2 < 50):
            return message_2[1]
        else:
            return message_2[2]

class BoxingGlove(Product):
    import random
    Boxing_ID = random.randint(1000000, 9999999)
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=Boxing_ID):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability
        self.identifier=identifier

    def explode(self):
        str = '...it is a glove.'
        return str

    def punch(self):
        message_3 = ["That tickles.", "Hey that hurt!", "Ouch!"]
        if(self.weight < 5):
            return message_3[0]
        elif(5 <= self.weight and self.weight < 15):
            return message_3[1]
        else:
            return message_3[2]