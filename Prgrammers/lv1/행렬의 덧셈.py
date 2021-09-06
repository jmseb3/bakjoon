def solution(arr1, arr2):
    answer = []
    for data1,data2 in zip(arr1,arr2):
        tmp =[]
        for x,y in zip(data1,data2):
            tmp.append(x+y)
        answer.append(tmp)
    return answer