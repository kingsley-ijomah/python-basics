class Matrix:
    def __init__(self, matrix_string):
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 7, 6]]
        self.matrix = [self.to_int(x) for x in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [x[index - 1] for x in self.matrix]

    def to_int(self, string):
        return [int(i) for i in string.split()]
