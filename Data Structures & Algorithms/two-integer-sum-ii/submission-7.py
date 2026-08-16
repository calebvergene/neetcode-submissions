class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        while i < len(numbers) - 2:
            l, r = i+1, len(numbers)-1
            other = target - numbers[i]
            while l <= r:
                mid = (r+l)//2
                if numbers[mid] == other:
                    return [i + 1, mid + 1]
                elif numbers[mid] < other:
                    l = mid + 1
                else:
                    r = mid - 1 
            i += 1
        return [len(numbers)-1, len(numbers)]