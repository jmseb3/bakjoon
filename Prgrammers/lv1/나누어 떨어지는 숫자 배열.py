def solution(arr, divisor):
    arr.sort()
    data = [i for i in arr if i % divisor == 0]
    return data if data else [-1]
