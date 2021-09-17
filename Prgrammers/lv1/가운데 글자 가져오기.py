def solution(s):
    std = len(s)//2
    return s[std] if len(s) % 2 == 1 else s[std-1:std+1]
