import datetime

def solution(a, b):
    weekday = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    dates = datetime.date(2016,a,b)
    return weekday[dates.weekday()]