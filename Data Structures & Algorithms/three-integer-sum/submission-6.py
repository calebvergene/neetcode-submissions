class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = 0

        def move(index, num):
            # skips duplicate numbers when increment/decrement
            original = nums[index]
            while nums[index] == original:
                index += num
            return index

        while l < len(nums)-2:
            m, r = l + 1, len(nums)-1
            while m < r:
                added = nums[l]+nums[m]+nums[r]
                if added == 0:
                    result.append([nums[l], nums[m], nums[r]])
                    m = move(m, 1)
                elif added > 0:
                    r = move(r, -1)
                else:
                    m = move(m, 1)
            l = move(l, 1)

        return result


