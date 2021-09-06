def solution(x):
    div_ = 0
    start = x
    while True:
        if start < 10:
            div_ += start
            break
        else:
            div_ += start % 10
            start //= 10
    if x % div_ == 0:
        answer = True
    else:
        answer = False
    return answer
