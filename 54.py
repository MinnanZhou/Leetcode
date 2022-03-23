def func(matrix):
    elements = len(matrix) * len(matrix[0])
    m, n = 0, 0
    step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    rb = len(matrix[0]) - 1
    db = len(matrix) - 1
    lb = 0
    ub = 0
    index = 0
    direction = 0
    ret = []
    while index < elements:
        index+=1
        ret.append(matrix[m][n])
        if n == rb and direction == 0:
            direction = 1
            ub += 1
        if n == lb and direction == 2:
            direction = 3
            db -= 1
        if m == db and direction == 1:
            direction = 2
            rb -= 1
        if m == ub and direction == 3:
            direction = 0
            lb += 1
        m = m + step[direction][0]
        n = n + step[direction][1]
    return ret


inp = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(func(inp))
