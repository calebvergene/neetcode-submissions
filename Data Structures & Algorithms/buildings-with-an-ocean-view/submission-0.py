class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1][0] <= height:
                stack.pop()
            stack.append((height, i))
        return [index for _, index in stack]