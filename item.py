import csv

class item:
    pay_rate = 0.8 # The pay rate is 20 % discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):


        # Run validation to recieved arguments
        assert price >= 0 , f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"

        # Assign to self object        
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to execute
        item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * item.pay_rate


    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property decorator = Read only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception ("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Haider.
        We have{self.name} {self.quantity} times.
        regards, JimShapedCoding
        """
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    
