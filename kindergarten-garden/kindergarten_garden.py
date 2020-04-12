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
        res = []
        for row in self.diagram:
            res.append([row[i:i+2] for i in range(0,len(row),2)])
        return res

    def fetch_plants(self, student):
        res = []
        plant_rows = self.plant_rows()
        for key,plant in enumerate(plant_rows):
            res.append(plant_rows[key][self.students.index(student)])
        return res

    def plants(self, student):
        res = []
        for initial in ''.join(self.fetch_plants(student)):
            res.append(PLANTS[initial])
        return res
    

