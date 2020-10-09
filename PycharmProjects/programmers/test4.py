
def solution(routes):
    answer = 0
    candidate = []
    cars = range(len(routes))
    for i in cars:
        for j in cars:
            start = routes[i][0]
            rangeL = range(routes[j][0], routes[j][1])
            if start in rangeL:
                if len(candidate) < i + 1:
                    candidate.append([j])
                else:
                    candidate[i].append(j)


    final = []
    for value in sorted(candidate, key = lambda item: len(item), reverse=True):
        flag = False
        for v in value:
            if v not in final:
                final.append(v)
                flag = True
                
        if flag : answer += 1
    print(answer)
    return answer


# solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
solution([[-20, 19], [-18, 17], [-15, 14], [-20, 15]])