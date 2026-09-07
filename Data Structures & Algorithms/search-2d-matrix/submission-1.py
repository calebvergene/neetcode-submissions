class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search rows, then cols
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        # l and r end up as a range. 
        arr = matrix[r]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False