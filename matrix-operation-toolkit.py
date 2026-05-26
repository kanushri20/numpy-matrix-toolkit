import numpy as np

def main():
        print("          Matrix Operation Toolkit")
        print("Hello! This is matrix operation app")
        print("""
        Enter:
            1 for matrix multiplication
            2 for calculation of determinant
            3 for finding inverse
            4 for finding eigen values
            5 for solving linear equation
            6 for exit
        """)
        while True:
            try:
                userInput = int(input("Enter your choice: "))
                if userInput == 1:
                    matrixMultiplication()
                elif 4 >= userInput >= 2:
                    print("This function determines the determinant of the give n x n matrix")
                    while True:
                        try:
                            size = int(input("Enter size of the Matrix: "))
                            break
                        except ValueError:
                            print("Only integer!!")
                    matrix = np.zeros([size, size], dtype=int)
                    for i in range(0, size):
                        for j in range(0, size):
                            while True:
                                try:
                                    matrix[i, j] = int(input(f"Enter value for {i + 1} row {j + 1} column: "))
                                    break
                                except ValueError:
                                    print("Integers Only!!")
                    if userInput == 2:
                        determinantCal(matrix)
                    elif userInput == 3:
                        inverseCal(matrix)
                    else:
                        eigenValueCal(matrix)
                elif userInput == 5:
                    linSolve()
                elif userInput == 6:
                    break
                else:
                    print("Invalid Entry")
            except ValueError:
                print("Only integer values!!")

def matrixMultiplication():
    while True:
        print("Please provide the size for the matrices such that the column of first matrix = row of second matrix: ")
        print("Matrix 1")
        r1 = int(input("    Enter size for row: "))
        c1 = int(input("    Enter size for column: "))
        print("Matrix 2")
        r2 = int(input("    Enter size for row: "))
        c2 = int(input("    Enter size for column: "))

        if c1 != r2:
            print("Matrix Multiplication not possible")
        else:
            mat1 = np.zeros((r1, c1), dtype=int)
            mat2 = np.zeros((r2, c2), dtype=int)
            print("Enter values: ")
            print("Matrix 1")
            for i in range (0, r1):
                for j in range (0, c1):
                    while True:
                        try:
                            mat1[i, j] = int(input(f"Enter {i} row {j} column value: "))
                            break
                        except ValueError:
                            print("Only integers!!")
            print("Matrix 1 Successful!\n", mat1)
            print("Enter values: ")
            print("Matrix 2")
            for i in range(0, r2):
                for j in range(0, c2):
                    while True:
                        try:
                            mat2[i, j] = int(input(f"Enter {i + 1} row {j + 1} column value: "))
                            break
                        except ValueError:
                            print("Only integers!!")

            print("Matrix 2 Successful!\n", mat2)
            mulMat = np.dot(mat1, mat2)
            print("Resultant matrix = \n", mulMat)
            break
def determinantCal(matrix):
        det = np.linalg.det(matrix)
        print("Determinant =", round(det, 2))
def inverseCal(matrix):
    try:
        inv = np.linalg.inv(matrix)
        print("Inverse Matrix =\n", inv)

    except np.linalg.LinAlgError:
        print("Inverse does not exist")
def eigenValueCal(matrix):
    values, vectors = np.linalg.eig(matrix)

    print("Eigen Values =")
    print(values)

    print("Eigen Vectors =")
    print(vectors)
def linSolve():
    size = int(input("Enter number of variables: "))

    A = np.zeros((size, size), dtype=int)

    print("Enter coefficients:")

    for i in range(size):
        for j in range(size):
            A[i, j] = int(input(f"Enter value for {i},{j}: "))

    B = np.zeros(size, dtype=int)

    print("Enter constants:")

    for i in range(size):
        B[i] = int(input(f"Equation {i} constant: "))

    try:
        solution = np.linalg.solve(A, B)
        print("Solution:")
        print(solution)

    except np.linalg.LinAlgError:
        print("No unique solution exists")

main()