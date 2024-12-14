class vehicle:
    def description(self):
        print("this is vehicle")

class engine:
    def engine_type(self):
        print("engine type is fuel")

class car(vehicle,engine):
    def wheels(self):
        print("car has 4 wheels")

car=car()
car.description()
car.engine_type()
