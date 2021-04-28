import sys
input = sys.stdin.readline

n = int(input())
n = bin(n)[2:]

matrix = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]


def martix_answer(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k]*b[k][j]) % 1000000007

    return result


for i in range(len(n)):
    if n[-i-1] == "1":
        temp = matrix[:]
        while i != 0:
            temp = martix_answer(temp, temp)
            i -= 1
        result = martix_answer(result, temp)

print(result[0][1] % 1000000007)
