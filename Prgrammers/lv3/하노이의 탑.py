

def solution(n):
    def han(n, first, final):
        if n == 1:
            return[[first, final]]
        return han(n-1, first, 6-first-final) + han(1, first, final) + han(n-1, 6-first-final, final)
    answer = han(n, 1, 3)
    return answer
