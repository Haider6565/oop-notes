from item import item

class phone(item):
    
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Call to cuper function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
        # Run validation to recieved arguments
        assert broken_phones >= 0, f"broken phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object        
        self.broken_phones = broken_phones


phone1 =  phone("jscphonev10", 500, 5)
#print(item.all)
#print(phone.all)