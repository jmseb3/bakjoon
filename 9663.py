def checkupdown(x,col):
    for i in range(1,x):
        if col == row[i] or abs(col- row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    for i in range(1,n+1):
        if checkupdown(x, i):
            row[x] = i
            if x < n:
                dfs(x+1)
            else:
                result +=1


n = int(input())
row = [0]*(n+1)
result =0
dfs(1)
print(result)