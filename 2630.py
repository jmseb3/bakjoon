
def quarter_square(x, y, n):
    global matrix, blue, white
    check = True
    first_color = matrix[x][y]

    for i in range(x, x+n):
        if not check:
            break

        for j in range(y, y+n):
            if matrix[i][j] != first_color:
                check = False
                k = n//2
                quarter_square(x,y,k)
                quarter_square(x+k, y, k)
                quarter_square(x, y+k, k)
                quarter_square(x+k, y+k, k)
                break

        if check:
            if first_color == 1:
                blue += 1
                return
            elif first_color == 0:
                white += 1
                return


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

quarter_square(0, 0, n)
print(white)
print(blue)
