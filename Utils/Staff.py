class Staff:
    def __init__(self, name, examine_person, department):
        self.id = id
        self.name = name
        self.examine_person = examine_person
        self.department = department

    def toString(self):
        return "#" + str(self.id) + "#" + self.examine_person + "@" + self.name + "# "