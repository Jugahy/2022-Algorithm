# My Code
def solution(point):
    count = 0

    x, y = ord(point[0]) - 96, int(point[1])

    move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    for i in move:
        nx = x + i[0]
        ny = y + i[1]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            nx, ny = 0, 0
        else:
            count += 1

    return count


# Good Code
def solution1(point):
    count = 0

    x, y = ord(point[0]) - 96, int(point[1])

    move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    for i in move:
        nx = x + i[0]
        ny = y + i[1]
        if 1 <= nx <= 8 and 1 <= ny <= 8:  # crazy detail
            count += 1

    return count
