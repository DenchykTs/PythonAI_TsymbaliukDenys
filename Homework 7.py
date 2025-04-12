class Sweets:
    def __init__(self, sweetness):
        self.sweetness = sweetness

    def __iter__(self):
        for i in range(self.sweetness):
            yield i

sweet_machine = Sweets(5)

for sw in sweet_machine:
    print(sw)





