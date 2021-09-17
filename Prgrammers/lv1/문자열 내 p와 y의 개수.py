def solution(s:str):
    cnt =0
    for x in s.lower():
        if x =='y':
            cnt +=1
        if x=='p':
            cnt -=1

    return cnt==0