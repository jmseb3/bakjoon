def solution(numbers, hand):
    def dist(a, b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

    answer = ''
    left = (3, 0)
    right = (3, 2)
    idx = [2, 5, 8, 0]
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = (number//3, 0)
        elif number in [3, 6, 9]:
            answer += 'R'
            right = (number//3-1, 2)
        else:
            now = (idx.index(number), 1)
            left_dist = dist(left, now)
            right_dist = dist(right, now)

            if left_dist<right_dist:
                answer +='L'
                left =now
            elif right_dist<left_dist:
                answer +='R'
                right =now
            else:
                if hand=='right':
                    answer+='R'
                    right = now
                else:
                    answer+='L'
                    left =now

    return answer
