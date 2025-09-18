#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith 
# line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
h = [1,8,6,2,5,4,8,3,7]
def maxArea(heights):
    if len(heights) < 2: return 0
    l = 0
    r = len(heights)-1
    maxArea = 0
    
    while l < r:
        current = min(heights[l], heights[r]) * (r-l)
        maxArea = max(maxArea, current)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return maxArea


print(maxArea(h))
