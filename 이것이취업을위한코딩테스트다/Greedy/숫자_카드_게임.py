# Good Code
def solution(n, m):
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))

        min_value = min(data)
        result = max(result, min_value)

    return result
