from collections import defaultdict


def solution(str1, str2):
    data1 = get_set(str1)
    data2 = get_set(str2)
    set1 = {k for k in data1.keys()}
    set2 = {k for k in data2.keys()}
    uni = set1.union(set2)
    data = defaultdict(lambda: [0, 0])
    for key in uni:
        temp = []
        temp.append(data1[key])
        temp.append(data2[key])
        temp.sort()
        data[key] = temp
    uni_val = 0
    inter_val = 0
    for v in uni:
        uni_val += data[v][1]
        inter_val += data[v][0]
    try:
        return int((inter_val/uni_val)*65536)
    except ZeroDivisionError:
        return 65536


def get_set(string: str):
    string = string.lower()
    res = defaultdict(int)
    for idx in range(len(string)-1):
        temp = string[idx:idx+2]
        if temp.isalpha():
            res[temp] +=1

    return res