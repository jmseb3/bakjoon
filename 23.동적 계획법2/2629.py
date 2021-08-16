import sys
input = sys.stdin.readline
n = int(input())
kg = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))


def solution(kg, finds):
    def check_set(set_, check):
        res = set(set_)
        for x in set_:
            tmp1 = x-check
            tmp2 = x+check
            if tmp1 <= 40000:
                res.add(abs(tmp1))
            if tmp2 <= 40000:
                res.add(abs(tmp2))
        return res

    ans = []
    dp = [set([0]) for _ in range(n)]
    dp[0].add(kg[0])

    for x in range(1, n):
        dp[x] = check_set(dp[x-1], kg[x])

    for find in finds:
        if find in dp[n-1]:
            ans.append("Y")
        else:
            ans.append("N")
    return ans


print(*solution(kg, find))
