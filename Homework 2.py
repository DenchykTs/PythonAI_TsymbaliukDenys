class Pet:
    amount_of_pets = 0
    print("This is our pets' live!")
    def __init__(self, name = None, happiness = 0):
        self.name = name
        Pet.amount_of_pets += 1
        self.happiness = happiness
        print(f"{self.name}.happiness - {self.happiness}")
        print(f"Hi my love!")

    def __str__(self):
        return(f"This is our pet. It's name is {self.name}.")

    def add_happiness(self):
        self.happiness += 15

print('_'*15, "Kaisy the cat", '_'*15)
Cat = Pet(name = "Kaisy")
Cat.add_happiness()
print(f"Cat.happiness - {Cat.happiness}")
print(Cat.amount_of_pets)
print(Cat)

print('_'*15, "Boby the dog", '_'*15)
Dog = Pet(name = "Boby")
Dog.add_happiness()
print(f"Dog.happiness - {Dog.happiness}")
print(Dog.amount_of_pets)
print(Dog)
