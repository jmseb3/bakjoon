n, m = map(int, input().split())
r = n - m


def count_n(x, n):
    ans = 0
    while x >= n:
        ans += x//n
        x //= n
    return ans


print(min(count_n(n, 2) - count_n(m, 2) - count_n(r, 2), count_n(n, 5) - count_n(m, 5) - count_n(r, 5)))