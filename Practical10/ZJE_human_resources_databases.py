# Classify the staff from four aspects and build a relationship between the aspects and the individual.
class Staff():
    def __init__(self, first, last, locations, roles):
        self.firstname = first
        self.lastname = last
        self.location = locations
        self.role = roles
# Define a function that shows the information positioning individuals.

    def printinfo(self):
        print(self.firstname, self.lastname, self.location, self.role)


employee = Staff(input("firstname"), input("lastname"),
                 input("location"), input("role"))
employee.printinfo()
