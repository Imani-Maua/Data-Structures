
class Solution:
  def threeSum(self, nums: list) -> list[list[int]]:
    nums.sort()
    triplets = []

    for i, num in enumerate(nums):
        if num > 0: break
        if i > 0 and num == nums[i-1]: continue
        right, left = len(nums)-1, i+1
        while left < right:
            total = num + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([num, nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                while nums[right] == nums[right+1] and left < right:
                    right -= 1
    return triplets
