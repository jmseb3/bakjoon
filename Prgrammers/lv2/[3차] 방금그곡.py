def solution(m, musicinfos):
    ch = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
    answer = ('(None)',None)
    for k, v in ch.items():
        m = m.replace(k, v)

    for musicinfo in musicinfos:
        start, end, title, sound = musicinfo.split(',')

        for k, v in ch.items():
            sound = sound.replace(k, v)

        h1, m1 = start.split(':')
        h2, m2 = end.split(':')
        time = (int(h2)-int(h1))*60 + int(m2)-int(m1)
        total_code = (sound * (int(time/len(sound))+1))[:time]

        if m in total_code:
            if (answer[1]==None) or (answer[1]<time):
                answer = (title,time)
    return answer[0]