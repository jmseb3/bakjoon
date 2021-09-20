import re

def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = dict() # 나를 가리키는 외부 링크
    
    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basicScore = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basicScore += 1
        exiosLink = re.findall('<a href="(https://[\S]*)"', page)
        
        for link in exiosLink:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)
        
        webpageName.append(url)
        webpage.append([url, basicScore, len(exiosLink)]) # 내가 가진 외부 링크 (개수)
        
    # 링크점수 = 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합
    # 매칭점수 = 기본점수 + 링크점수
    maxValue = 0
    result = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        
        if url in webpageGraph.keys():
            # 나를 가리키는 다른 링크의 기본점수 ÷ 외부 링크 수의 총합을 구하기 위해
            for link in webpageGraph[url]: 
                a, b, c = webpage[webpageName.index(link)]
                score += (b / c)
        
        if maxValue < score:
            maxValue = score
            result = i
    
    return result