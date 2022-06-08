# My Code
def solution(point):
    count = 0

    x, y = ord(point[0]) - 96, int(point[1])

    move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if dx < 1 or dy < 1 or dx > 8 or dy > 8:
            dx, dy = 0, 0
        else:
            count += 1

    return count


# Good Code
def solution1(point):
    count = 0

    x, y = ord(point[0]) - 96, int(point[1])

    move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if 1 <= dx <= 8 and 1 <= dy <= 8:  # crazy detail
            count += 1

    return count
