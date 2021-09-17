def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for idx in range(len(word)):
            answer += word[idx].upper() if idx % 2 == 0 else word[idx].lower()
        answer += ' '

    return answer[:-1]
