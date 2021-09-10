def solution(arr):
    def quad_tree(x,y,n):
        check = False
        ck = arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != ck:
                    check = True
                    break
        
        if check:
            k=n//2
            quad_tree(x,y,k)
            quad_tree(x,y+k,k)
            quad_tree(x+k,y,k)
            quad_tree(x+k,y+k,k)
        else:
            answer[arr[x][y]] +=1

    answer = [0,0]

    quad_tree(0,0,len(arr))
    return answer