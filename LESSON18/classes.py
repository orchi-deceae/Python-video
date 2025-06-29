class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f'I\'m a {self.make} {self.model}.')

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Caldillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print('Flies along..')
    
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')
    
class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('mack', 'pinna')
swaggon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

swaggon.get_make_model()
swaggon.moves()

print('\n\n')

for i in (my_car, your_car, cessna, mack, swaggon):
    i.get_make_model()
    i.moves()
    print()


# Classes are javascript objects for functions 
# objects are functions
# innit are parms:

# innit creates a js object with the codeName "self"
# so innit creates:
#     self = {
#         ver1: 1
#         ver2: 2
#         ver3: 3
#     }
