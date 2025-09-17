intervals =[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4, 8]
def insert(intervals, newInterval):
    if not len(newInterval) and not len(intervals):
        return []
    
    if not len(newInterval):
        return [intervals]
    
    if not len(intervals):
        return [newInterval]
    
    inserted = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        inserted.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0],intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    inserted.append(newInterval)
    
    while i < n and intervals[i][0] > newInterval[0]:
        inserted.append(intervals[i])
        i += 1
    return inserted
    



print(insert(intervals, newInterval))


    
    
