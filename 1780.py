import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

paper_one, paper_zero, paper_minuseone = 0, 0, 0

def ispaper(x, y, n):
    global paper, paper_one, paper_zero, paper_minuseone
    check = False
    first_color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if first_color != paper[i][j]:
                check = True
                break

    if check:
        k = n//3
        ispaper(x, y, k)
        ispaper(x, y+k, k)
        ispaper(x, y+2*k, k)

        ispaper(x+k, y, k)
        ispaper(x+k, y+k, k)
        ispaper(x+k, y+2*k, k)

        ispaper(x+2*k, y, k)
        ispaper(x+2*k, y+k, k)
        ispaper(x+2*k, y+2*k, k)
    else:
        if first_color == -1:
            paper_minuseone += 1
        elif first_color == 0:
            paper_zero += 1
        elif first_color == 1:
            paper_one += 1
            
ispaper(0, 0, n)

print(paper_minuseone)
print(paper_zero)
print(paper_one)
