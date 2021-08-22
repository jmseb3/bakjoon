from collections import deque

N, K = map(int, input().split())

MAX_NUM = 100_001
dp = [[int(1e9), list()]] * (100_001)
dp[5] = [0, [5]]


def possible(a):
    if 0 <= a <= 100_001:
        return True
    return False


q = deque()
q.append(N)

while q:
    now = q.popleft()
    if now == K:
        print()
