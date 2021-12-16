def partition(mtx):
    sub1 = sub2 = sub3 = sub4 = mtx
    while len(sub1) > len(mtx) // 2:
        #collumn partition
        sub1 = sub1[:len(sub1) // 2]
        sub2 = sub2[:len(sub2) // 2]
        sub3 = sub3[len(sub3) // 2:]
        sub4 = sub4[len(sub4) // 2:]
    while len(sub1[0]) > len(mtx[0]) // 2:
        for i in range(len(sub1[0])//2):
            #row partition
            sub1[i] = sub1[i][:len(sub1[i])//2]
            sub2[i] = sub2[i][len(sub2[i])//2:]
            sub3[i] = sub3[i][:len(sub3[i])//2]
            sub4[i] = sub4[i][len(sub4[i])//2:]
    return sub1, sub2, sub3, sub4

def matrix_add(A, B):
    n = len(A)
    total = [[None for j in range(0, n)] for i in range(0, n)]
    for i in range(n):
        for j in range(n):
            total[i][j] = A[i][j] + B[i][j]
    return total

def matrix_minus(A, B):
    n = len(A)
    total = [[None for j in range(0, n)] for i in range(0, n)]
    for i in range(n):
        for j in range(n):
            total[i][j] = A[i][j] - B[i][j]
    return total
    
def strassen(A, B):
    if len(A) == 1:
        C = [[None]]
        C[0][0] = A[0][0] * B[0][0]
        return C
    
    sub1, sub2, sub3, sub4 = partition(A)
    sub5, sub6, sub7, sub8 = partition(B)

    s1 = matrix_minus(sub6, sub8)
    s2 = matrix_add(sub1, sub2)
    s3 = matrix_add(sub3, sub4)
    s4 = matrix_minus(sub7, sub5)
    s5 = matrix_add(sub1, sub4)
    s6 = matrix_add(sub5, sub8)
    s7 = matrix_minus(sub2, sub4)
    s8 = matrix_add(sub7, sub8)
    s9 = matrix_minus(sub1, sub3)
    s10 = matrix_add(sub5, sub6)

    p1 = strassen(sub1, s1)
    p2 = strassen(s2, sub8)
    p3 = strassen(s3, sub5)
    p4 = strassen(sub4, s4)
    p5 = strassen(s5, s6)
    p6 = strassen(s7, s8)
    p7 = strassen(s9, s10)

    c11 = matrix_add(matrix_minus(matrix_add(p5, p4), p2), p6)
    c12 = matrix_add(p1, p2)
    c21 = matrix_add(p3, p4)
    c22 = matrix_add(matrix_minus(matrix_minus(p5, p3), p7), p1)

    
    C = [[None for row in range(len(c11) * 2)] for col in range(len(c11) * 2)]
    for i in range(len(c11)):
        for j in range(len(c11)):
            C[i][j] = c11[i][j]
            C[i][j + len(c11)] = c12[i][j]
            C[i + len(c11)][j] = c21[i][j]
            C[i + len(c11)][j + len(c11)] = c22[i][j]
    return C


a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
b = [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]


print(strassen(a, b))






    
