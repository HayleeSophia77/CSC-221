
class Person:
    def __init__(first, last, phone):
        self.__first = first
        self._last = last
        self.__phone = phone

    def set_first(name):
        self.__first = name

    def get_last(last):
        self.__last = last

    def set_phone(phone):
        self.__phone = phone
    
    def get_first(self):
        return self.__first
        
    def get_last(self):
        return self.last
    
    def get_phone(self):
        return self.phone
    
    def __repr__(self):

        return f'{first:<20}{last:<20}{get_phone()<20}'

class Customer(self.Person):
    def __init__(first, last,phone, email, state, address):
        
        self.__first = first
        self.__last = last
        self.__email = email
        self._state = state
        self._address = address
 
     
    #Setters
    def set_email(self):
        self.__email = email
    def set_address(self,address):
        self._address = address
    def set_state(state):
        self.__state = state
  
    #Getters   
    def get_email():
        return email

    def get_address():
        return self._address
    
    def get_state(self):
        return self.__state
    
    def __repr__(self):

        return Person._repr_()+f'{self.get_address():<20}{self.get_state()}'
  
        




