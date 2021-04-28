import sys

input = sys.stdin.readline

def martix_answer(a, b):
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for t in range(n):
                result[i][j] += a[i][t]*b[t][j]
                result[i][j] %= 1000

    return result


n, b = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 2진법 변환
b = bin(b)[2:]

# 단위행렬
identity_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    identity_matrix[i][i] = 1

# 2의제곱단위로 쪼개서 계산실행
result = identity_matrix[:]
for i in range(len(b)):
    # 2진법에서 1이라면
    if b[-i-1] == '1':
        temp = matrix[:]
        # 그만큼 제곱실행
        while i != 0:
            temp = martix_answer(temp, temp)
            i -= 1
        # 값 반환
        result = martix_answer(result, temp)

for k in result:
    print(*k)
