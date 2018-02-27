class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_saved=0
    def describe_restaurant(self):
        print("The restaurant called "+self.name.title())
        print('The restaurant is a '+self.cuisine_type.title()+' flavor.')
    def open_restuarant(self):
        print('The restaurant is open now!')
    def read_number(self):
        print('The saved number is '+str(self.number_saved))
    def set_number_saved(self, number):
        self.number_saved=number
    def increment_number_served(self,n):
        self.number_saved+=n
        
my_restaurant=Restaurant('Yun Hai Yao','Yun nan')
my_restaurant.set_number_saved(23)
my_restaurant.increment_number_served(100)
my_restaurant.read_number()

