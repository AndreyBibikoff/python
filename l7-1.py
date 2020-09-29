class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __add__(self):
        new_matrix = [[0, 0], [0, 0], [0, 0]]

        for i in range(len(self.matrix_1)):

            for j in range(len(self.matrix_2[i])):
                new_matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_1]))


matrix_1 = Matrix([[5, 18], [6, 17], [41, 50]], [[45, 8], [6, 7], [24, 5]])

print(f'Матрица: \n{matrix_1.__str__()}')
print(f'Сумма матриц: \n{matrix_1.__add__()}')

