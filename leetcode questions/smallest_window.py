def smallestWindow(arr):
    if len(arr) < 3:
        return -1
    min_len = float('inf')
    left = 0
    freq = {}
    for right in range(len(arr)):
        if arr[right] == '1' or arr[right] == '2' or arr[right] == '0':
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            while len(freq) == 3:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left+=1
            min_len = min(min_len, (right+1) - left)
    if min_len == float('inf'):
        return -1
    return min_len





