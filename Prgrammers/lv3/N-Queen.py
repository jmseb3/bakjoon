answer =0
def solution(n):
    global answer
    row = [0]*(n+1)

    def checkupdown(x, col):
        for i in range(1, x):
            if col == row[i] or abs(col-row[i]) == x-i:
                return False
        return True

    def dfs(x):
        global answer
        for i in range(1, n+1):
            if checkupdown(x, i):
                row[x] = i
                if x < n:
                    dfs(x+1)
                else:
                    answer += 1

    dfs(1)

    return answer
