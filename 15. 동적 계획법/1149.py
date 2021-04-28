n = int(input())
pay =[list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    # 윗층에 있는 다른 색중 최솟값을 더해나감
    pay[i][0] += min(pay[i-1][1], pay[i-1][2])
    pay[i][1] += min(pay[i-1][0], pay[i-1][2])
    pay[i][2] += min(pay[i-1][0], pay[i-1][1])

# 최종 마지막중 작은것을 출력
print(min(pay[n-1][0],pay[n-1][1],pay[n-1][2]))