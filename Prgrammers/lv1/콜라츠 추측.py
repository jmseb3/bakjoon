# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    while True:
        if answer>=500:
            return -1
        if num ==1:
            break

        if num%2==0:
            num //=2
        else:
            num *=3
            num+=1
        answer+=1

    return answer