class Seed:
     ripening_force = 25
     consumption = 10
     benefit = 5
     def __init__(self):
         print("Seed (1 level)")
         print('-' * 35)
         print(f"ripening_force = {self.ripening_force}")
         print(f"consumption = {self.consumption}")
         print(f"benefit = {self.benefit}")

s = Seed()

class Sprout(Seed):
    ripening_force = 30
    consumption = 5
    the_power_of_flourishing = 15
    attractiveness = 5
    photosynthesis = 5
    def __init__(self):
        print('-' * 35)
        print("Sprout (2 level)")
        print('-' * 35)
        print(f"ripening_force = {self.ripening_force}")
        print(f"consumption = {self.consumption}")
        print(f"benefit = {self.benefit}")
        print(f"the_power_of_flourishing = {self.the_power_of_flourishing}")
        print(f"attractiveness = {self.attractiveness}")
        print(f"photosynthesis = {self.photosynthesis}")

sp = Sprout()

class Flower(Sprout):
    ripening_force = 50
    the_power_of_flourishing = 30
    attractiveness = 65
    pollination = 25
    benefit = 15
    consumption = 7
    photosynthesis = 40
    def __init__(self):
        print('-' * 35)
        print("Flower (3 level)")
        print('-' * 35)
        print(f"ripening_force = {self.ripening_force}")
        print(f"consumption = {self.consumption}")
        print(f"benefit = {self.benefit}")
        print(f"the_power_of_flourishing = {self.the_power_of_flourishing}")
        print(f"attractiveness = {self.attractiveness}")
        print(f"pollination = {self.pollination}")
        print(f"photosynthesis = {self.photosynthesis}")

f = Flower()