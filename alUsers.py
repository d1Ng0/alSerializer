import random

class User:
    """
    User class. This class contains personal details for a user.
    The class keep offers getters and setters to allow modification of the individual user at later stage.
    Uses encapsulation to prevent changing data with invalid information    
    """
    
    def __init__(self, name, surname, phone, address):
        """
        @TODO: check for data types
        """
        self.name = name
        self.surname = surname
        self.phone = phone        
        # create an address instance
        self.address = Address()
        self.address.address_from_string(address)

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def __str__(self):
        """
        method for boxing obj > str
        """
        s = "{:15} {:15} {:<12} {:20}".format(self.name, self.surname, self.phone, self.address.__str__())
        return s

class Address:
    """
    Address class. Rather than storing the address into a string, we use a class to reinforce the 
    components of a valid address: street, city, state and zip code. 
    Having an address class might come in handy when the information are input from a user interface.
    """

    def __init__(self):
        self.street : str
        self.city: str
        self.state: str
        self.zipcode: int

    def address_from_string(self, aString):
        # isolate address information from string
        s = aString.split(',')
        if len(s) == 2:
            self.street = s[0]
            s = s[1].split()
            self.city = s[0]
            self.state = s[1]
            self.zipcode = s[2]
            return True
        else:
            return False

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

    def set_street(self, street):
        """
        TODO: ADD CHECKERS FOR ALL SETTERS
        """
        self.street = street
        return self.street

    def set_city(self, city):
        self.city = city
        return self.city

    def set_state(self, state):
        self.state = state
        return self.state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
        return self.zipcode

    def __str__(self):
        s = "{}, {} {} {}".format(self.street,self.city,self.state,self.zipcode)
        return s
