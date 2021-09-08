from collections import defaultdict, deque


def solution(board, moves):
    answer = 0
    data = defaultdict(lambda: deque())
    stack =[]
    for row in board:
        for idx in range(len(row)):
            if row[idx] != 0:
                data[idx+1].append(row[idx])
    for move in moves:
        if data[move]:
            next = data[move].popleft()
            if stack and stack[-1] ==next:
                stack.pop()
                answer +=2
            else:
                stack.append(next)
        
    return answer
