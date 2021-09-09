def solution(arr1, arr2):
    def res(row1,row2):
        cnt =0
        for x,y in zip(row1,row2):
            cnt +=x*y
        return cnt
    
    arr2 = list(zip(*arr2))
    answer = [[0]*len(arr2) for _ in range(len(arr1))]
    for y in range(len(arr1)):
        for x in range(len(arr2)):
            answer[y][x] = res(arr1[y],arr2[x])

    return answer