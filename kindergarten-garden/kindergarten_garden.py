STUDENTS = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Eve',
    'Fred',
    'Ginny',
    'Harriet',
    'Ileana',
    'Joseph',
    'Kincaid',
    'Larry'
]
PLANTS = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}

class Garden:
    def __init__(self, diagram, students = STUDENTS):
        self.diagram = diagram.split('\n')
        self.students = sorted(students) 

    def plant_rows(self):
        for row in self.diagram:
            yield [row[i:i+2] for i in range(0,len(row),2)]

    def plant_initials(self, student):
        plant_rows = list(self.plant_rows())
        for key,plant in enumerate(plant_rows):
            yield plant_rows[key][self.students.index(student)]

    def plants(self, student):
        return [PLANTS[initial] for initial in ''.join(self.plant_initials(student))]
    

