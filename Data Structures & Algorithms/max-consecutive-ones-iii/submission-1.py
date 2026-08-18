class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # have a queue of the k zeros
        q = collections.deque()

        # l tracks the zeros and increments to next zero if hash.len > k
        l, r = 0, 0 
        max_consecutive = 0

        while r < len(nums):
            if nums[r] == 0:
                q.append(r)
            r += 1
            if len(q) > k:
                # too many 0s in the window
                first_zero = q.popleft()
                l = first_zero + 1
            max_consecutive = max(max_consecutive, r-l)

        return max_consecutive

            