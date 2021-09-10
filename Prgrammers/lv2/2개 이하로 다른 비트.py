def solution(numbers):
    answer = []
    for num in numbers:
        if num %2 ==0:
            answer.append(num+1)
        else:
            bin_num = str(format(num,'b'))
            point = bin_num.rfind('01')
            if point ==-1:
                bin_num = '10' + bin_num[1:]
                answer.append(int(bin_num,2))
            else:
                bin_num = bin_num[:point]+'10'+bin_num[point+2:]
                answer.append(int(bin_num,2))
    return answer