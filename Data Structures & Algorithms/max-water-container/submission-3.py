class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so you want to maximize width and the second largest
        l, r = 0, len(heights)-1
        largest_area = 0
        while l <= r:
            area = min(heights[l], heights[r]) * (r-l)
            largest_area = max(largest_area, area)
            # move the smaller forward 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return largest_area