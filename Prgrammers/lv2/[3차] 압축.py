def solution(msg):
    data = {}
    for x in range(65, 91):
        data[chr(x)] = x-64
    answer = []
    w = ''
    for word in msg:
        if w+word in data.keys():
            w += word
            continue
        else:
            answer.append(data[w])
            data[w+word] = len(data)+1
            w = word
    answer.append(data[w])
    return answer
