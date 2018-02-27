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
my_restaurant=Restaurant('Yun Hai Yao','Yun nan')
print(my_restaurant.number_saved)
