class Staff:
    def __init__(self, staff_id, name, examine_person, department):
        self.staff_id = staff_id
        self.name = name
        self.examine_person = examine_person
        self.department = department

    def toString(self):
        return "#" + str(self.staff_id) + "#" + self.examine_person + "@" + self.name + "# "
