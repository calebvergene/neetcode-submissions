class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # need to binary search to find closest index to x
        l, r = 0, len(arr)-1
        while l < r:
            mid = (l+r)//2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        
        # set r and l to the closest one to x 
        if l > 0:
            l -= 1
        r = l
        print(l)
        # then two pointer out finding the k closest ints to x
        while (r-l+1)< k:
            # l closer to x
            if r >= len(arr)-1 or (l > 0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                l -= 1
            else:
                r += 1 

        return arr[l:r+1]