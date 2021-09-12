from copy import deepcopy
def solution(s):
    data =[]
    temp = set()
    for x in s[2:-2].split('},{'):
        temp =set()
        for num in x.split(','):
            temp.add(int(num))
        data.append(temp)
        
    data.sort(key=lambda x: len(x))
    visited =set()
    answer =[]
    for x in data:
        temp = x-visited
        answer.append(temp.pop())
        visited.update(x)
        
    return answer