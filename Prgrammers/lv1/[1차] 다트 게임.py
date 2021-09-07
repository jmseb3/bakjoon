def solution(dartResult):

    def ch(string, mul):
        if string == 'k':
            string = 10
        else:
            string = int(string)

        if mul == 'S':
            return string
        if mul == 'D':
            return string**2
        if mul == 'T':
            return string**3
    # 임시값
    dart = [0]
    now = 0
    # 10을 k로 변환시켜 한자리로 볼수있게함
    dartResult= dartResult.replace('10','k')
    print(dartResult)
    for idx in range(len(dartResult)):
        # 만약 SDT중 하나라면
        if dartResult[idx] in ['S', 'D', 'T']:
            now += 1
            # 앞에 숫자를 SDT에 맞게 변환시킴
            number = ch(dartResult[idx-1], dartResult[idx])
            # 그리고 추가함
            dart.append(number)
            # 만약 idx+1이 길이와 같다면 마지막에 왓으므로 넘어감
            if idx+1 == len(dartResult):
                continue
            # #이라면 해당 값을 -1배
            if dartResult[idx+1] == '#':
                dart[now] *= -1
            #  *이라면 지금과 이전값을 두배
            if dartResult[idx+1] == '*':
                dart[now] *= 2
                dart[now-1] *= 2
    return sum(dart)

