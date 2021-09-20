def solution(s):
    answer = []
    
    for word in s : 
        count=0
        st = ""
        for i in range(len(word)):
            #만약 st에 쌓은 것 앞의 2개가 "11"일 경우 count를 갱신해주고, st도 빼줍니다.
            if word[i] =="0" and st[-2:] == "11":
                st = st[:-2]
                count+=1
            else : 
                st += word[i]
        
        print(st)
        idx = st.find("11") 
        #"11"을 찾고 있으면 그 다음 인덱스에 다 넣습니다.
        #없으면 rfind(뒤에서 0을 찾아)그 앞에 다 넣습니다.
        if idx == -1:
            idx2 = st.rfind("0")
            st = st[:idx2+1] + "110" * count + st[idx2+1:]
        else : 
            st = st[:idx] + "110" * count +st[idx:]
        answer.append(st)                
                
    return answer
print(solution(["1110","100111100","0111111010"]))