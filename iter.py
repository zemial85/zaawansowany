class Klasa_1a:
    def __init__(self):
        self.students = []
        self.id = "1a"

    def add_student(self, student):
        self.students.append(student)
        return self.students

    def __iter__(self):
        return iter(self.students)


klasa1a = Klasa_1a()
klasa1a.add_student("Marek")
klasa1a.add_student("Zosia")

print(klasa1a.students)

for student in klasa1a:
    print(student)
