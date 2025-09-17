def maxSum(arr, k):
    n = len(arr)
    current_sum = sum(arr[:k])
    max_sum = sum(arr[:k])

    for i in range(k, n):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum


