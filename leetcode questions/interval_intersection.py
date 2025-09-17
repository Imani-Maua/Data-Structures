first  = [[0,2],[5,10],[13,23],[24,25]]  
second = [[1,5],[8,12],[15,24],[25,26]]

def intervalIntersection(first, second):
    if not first or not second:
        return [] 
    intersected = []
    f, s = 0, 0

    while f < len(first) and s < len(second):
        start = max(first[f][0], second[s][0])
        end = min(first[f][1], second[s][1])
        if start <= end:
            intersected.append([start, end])
        if first[f][1] < second[s][1]:
            f += 1
        else:
            s += 1

    return intersected




print(intervalIntersection(first, second))