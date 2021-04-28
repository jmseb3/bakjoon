n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    if i ==1:
        tri[1][0] += max(tri[0])
        tri[1][1] += max(tri[0])
    else:
        for j in range(i+1):
            if j == 0:
                tri[i][0] += tri[i-1][0]

            elif j < i:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

            else:
                tri[i][i] += tri[i-1][i-1]
    
print(max(tri[n-1]))
    

