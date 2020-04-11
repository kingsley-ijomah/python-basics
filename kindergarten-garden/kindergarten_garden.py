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
    def __init__(self, diagram, students):
        rows = diagram.split('\n')
