# My Code
def BigNum(m, k, num):
    i, j, answer = 0, 0, 0
    num.sort(reverse=True)

    while i < m:
        while j < k and i < m:
            answer += num[0]
            j += 1
            i += 1
        answer += num[1]
        i += 1
        j = 0
    return answer


# Good Code
def BigNum2(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += count * first
    result += (m - count) * second
    return result


