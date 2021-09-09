def solution(s:str):
    s = s.lower()
    ans=''
    for idx in range(len(s)):
        if idx ==0:
            if s[idx].isalpha():
                ans +=s[0].upper()
            else:
                ans+= s[0]
            continue
        if s[idx].isalpha() and s[idx-1]==' ':
            ans +=s[idx].upper()
        else:
            ans+=s[idx]


    return ans