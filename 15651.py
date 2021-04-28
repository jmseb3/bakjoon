n, m = map(int, input().split())
check = [False] * n
out = []

def recusive(index):
    if index == m:
        print(*out)
        return
        
    for i in range(n):

        if not check[i]:
            for k in range(i):
                check[k] =True
            out.append(i+1)

            recusive(index+1)
            out.pop()

            for j in range(i, n):
                check[j] = False

recusive(0)