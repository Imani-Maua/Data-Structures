nums = [1,1,1,2,2,3]
k = 2
def topKFrequent(nums, k):
    n = dict()
    result = list()
    for num in nums:
        n[num] = n.get(num, 0) + 1
    for key,_ in sorted(n.items(), key=lambda x:(-x[1], x[0])):
        result.append(key)
    return result[:k]


print(topKFrequent(nums, k))