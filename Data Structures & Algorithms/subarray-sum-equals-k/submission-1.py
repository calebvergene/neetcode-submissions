class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subset_sums = defaultdict(int)
        subset_sums[0] += 1 # to handle not subtracting left subarray

        total = 0
        subarrays = 0 
        for num in nums:
            total += num
            subarrays += subset_sums[k-total]
            subset_sums[-total] += 1
        return subarrays