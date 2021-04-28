def quater_square(x, y, n):
    global matrix
    check = False #나눌수있는지 확인
    color = matrix[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if matrix[i][j] != color:
                check =True
                break
    # 나눌수 있는지 확인

    # 나눌수 있다면 ()로 감싸서 출력   
    if check:
        k =n//2
        print("(",end="")
        quater_square(x,y,k)
        quater_square(x,y+k,k)
        quater_square(x+k,y,k)
        quater_square(x+k,y+k,k)
        print(")",end="")
    # 아니라면 처음 color를 출력
    else:
        print(color,end="")


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input())))

quater_square(0,0,n)

