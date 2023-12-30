def matmul(A, B):
    if len(A[0]) != len(B):
        raise ValueError("The two matrices are not compatible for Multiplication")

    m3 = [[] for i in range(len(A))]  # created matrix of required final dimensions

    for i in range(len(A)):  # iterates through ROWS of 1st matrix
        for j in range(len(B[0])):  # iterates through COLUMNS of 2nd matrix
            s = 0

            for k in range(len(B)):  # iterates through ROWS of 2nd matrix
                s += A[i][k] * B[k][j]  # multiplying corresponding matrix elements

            m3[i].append(s)  # inserting the multiplied value in the ith row of new matrix

    return m3
