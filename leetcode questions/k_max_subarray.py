# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k

nums = [2, 1, 5, 1, 3, 2]
k = 3


def kMaxArray(nums, k):
   current_sum = sum(nums[:k])
   max_array = sum(nums[:k])

   for i in range(k, len(nums)):
      current_sum += nums[i] - nums[i-k]
      max_array = max(max_array, current_sum)
   return max_array


print(kMaxArray(nums, k))


   