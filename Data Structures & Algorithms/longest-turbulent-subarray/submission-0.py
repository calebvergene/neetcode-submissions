class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # sliding window, set l to r when no longer different 
        l = 0
        longest = 2
        for r in range(2, len(arr)):
            prevprev, prev, curr = arr[r-2], arr[r-1], arr[r]
            if prevprev < prev > curr or prevprev > prev < curr:
                longest = max(longest, r - l + 1)
            else:
                l = r-1

        return longest