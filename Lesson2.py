class Student:
    amount_of_student = 0
    print("Hi")
    def __init__(self, name = None, scholarship = 50 ):
        self.name = name
        self.height = 170
        print("I am alive!")
        Student.amount_of_student += 1
        self.scholarship = scholarship
        # self.scholarship += 100

    def __str__(self):
        return(f"I am Student. My name is {self.name}")

    def add_scholarship(self):
        self.scholarship += 100

    def __del(self):
        print(f"The student {self.name} is no longer enrolled at the university.")


print('-'*10, "tom", "-"*10, sep="")
tom = Student(name = "Tom", scholarship = 100)
tom.add_scholarship()
print(tom.amount_of_student)
print(f"scholarship tom - {tom.scholarship}")
print(tom)


print('-'*10, "bill", "-"*10, sep="")
bill = Student(name = "Bill")
bill.add_scholarship()
print(bill.amount_of_student)
print(f"scholarship bill - {bill.scholarship}")
print(bill)


print(f"tom.height - {tom.height}")
print(f"bill.height - {bill.height}")
tom.height = 180
print('-'*30)
print(f"tom.height - {tom.height}")
print(f"bill.height - {bill.height}")

