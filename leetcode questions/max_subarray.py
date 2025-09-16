class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        maxArray = nums[0]

        for i in range(1, len(nums)):
            maxArray = max(maxArray + nums[i], nums[i])
            current_max = max(current_max, maxArray)
        
        return current_max
            



