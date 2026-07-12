class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if out of bounds:
        if x > arr[-1]: 
            l, r = len(arr)-1, len(arr)-1
        elif x < arr[0]:
            l, r = 0, 0
        # then need to binary search to find closest index to x
        else:
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
        
        # set r and l to the closest one to x 
        l = min([l, r], key=lambda a : abs(arr[a]-x))
        r = l
        # then two pointer out finding the k closest ints to x
        res = []
        while (r-l+1)< k:
            # l closer to x
            if r >= len(arr)-1 or (l > 0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                l -= 1
                print()
            else:
                r += 1 

        for i in range(l, r+1):
            res.append(arr[i])
        return res