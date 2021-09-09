def solution(s):
    data = list(map(int,s.split(' ')))
    data.sort()
    answer = str(data[0])+' '+str(data[-1])
    return answer