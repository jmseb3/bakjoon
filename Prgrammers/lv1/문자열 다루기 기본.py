def solution(s):
    N = len(s)
    if N == 4 or N == 6:
        try:
            s = int(s)
            return True
        except (ValueError):
            return False

    else:
        return False


print(solution("a234"))
