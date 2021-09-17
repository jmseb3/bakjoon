def solution(phone_number):
    N = len(phone_number)
    star = '*'*(N-4)
    answer = star + phone_number[N-4:N+1]
    return answer