class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
dave = Human("Dave")
lisa = Human("Lisa")
anna = Human("Anna")
maxim = Human("Maxim")
sasha = Human("Sasha")

car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()

car1 = Auto("BMW")
car1.add_passenger(dave)
car1.add_passenger(lisa)
car1.add_passenger(anna)
car1.add_passenger(maxim)
car1.add_passenger(sasha)
car1.print_passengers_names()





