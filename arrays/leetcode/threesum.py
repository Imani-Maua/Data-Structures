nums = [0, 0, 0]

def threeSum(nums: list):
    nums.sort()
    triplets = []
    for i in range(len(nums)-2):
        if nums[0] > 0: break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        right, left = len(nums)-1, i+1
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            while nums[left] == nums[left-1] and left < right:
                left += 1
            while nums[right] == nums[right+1] and left < right:
                right -= 1
            
    return triplets

print(threeSum(nums))   
        


