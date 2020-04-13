class School:
    def __init__(self):
        self.database = []

    def add_student(self, name, grade):
        self.database.append({'name':name, 'grade':grade})

    def roster(self):
        return [record['name'] for record in self.database_sorted()]

    def database_sorted(self):
        return sorted(self.database, key=lambda v: [v['grade'], v['name']])

    def grade(self, grade_number):
        return [record['name'] for record in self.database_sorted() if record['grade'] == grade_number]
