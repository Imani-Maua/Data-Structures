nums = [-1, -1, 1]
k = 0


def subarraySum(nums, k):
    countMap = {0: 1}
    count = 0
    prefixSum = 0

    for num in nums:
        prefixSum += num
        count += countMap.get((prefixSum - k), 0)
        countMap[prefixSum] =countMap.get(prefixSum, 0) + 1
    return count



print(subarraySum(nums, k))

