def matrix_threshold():
    initial = input().strip()
    M, N, threshold = [int(x) for x in initial.split(" ")]
    matrix = []
    for i in range(N):
        line = input().strip()
        matrix.append([int(x) for x in line.split(" ")])
    for i in range(N):
        if any(num <= threshold for num in matrix[i]):
            matrix[i] = [threshold for x in range(M)]
    print(matrix)


x = [[3, 2, 2],[1, 2, 3],[4, 5, 6]]
matrix_threshold()