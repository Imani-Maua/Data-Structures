
def merge(arr):
    if not len(arr): 
        return []
    if len(arr) == 1:
        return arr
    arr.sort(key=lambda x: x[0])
    merged = []
    merged.append(arr[0])
    for i in range(1, len(arr)):
        start, end = arr[i]
        if start <= merged[-1][1]:
            pass
            merged[-1][1] = (max(merged[-1][1], end))
        else:
            merged.append([start, end])
        
    return merged

