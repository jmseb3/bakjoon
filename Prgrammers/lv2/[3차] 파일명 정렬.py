import re


def solution(files):
    answer = []
    for file in files:
        idx_file = re.search('\d+', file)
        start_idx = idx_file.start()
        last_idx = idx_file.end()

        if last_idx-start_idx > 5:
            last_idx = start_idx+5

        answer.append([file[:start_idx].lower(),int(file[start_idx:last_idx]),file])
    answer.sort(key= lambda x:(x[0],x[1]))
    return [ans[2] for ans in answer]
