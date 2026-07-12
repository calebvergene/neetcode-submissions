class Solution:
    def numDecodings(self, s: str) -> int:
        # ways increases if the numbers can be combined. 
        # if combined, ways = (i+1)+(i+2)
        memo = ([False] * (len(s)-1)) + [1,1]
        if s == "0":
            return 0

        def decode(index):
            # top to bottom approach
            # base case: out of bounds or already exists in the cache
            if memo[index]:
                return memo[index]
            # if come across a 0, needs to be connected at the front
            if s[index] == '0':
                return 0

            # basically, starting from the end, calculate ways for each letter then store it
            ways = 0
            ways += decode(index+1)

            # if i and i+1 can be combined, then you need to calculate the # of ways for (i+1) and (i+2)
            # which should be already stored. 
            if (int(s[index])*10) + int(s[index+1]) <= 26:
                ways += decode(index+2)

            # store ways then return it
            memo[index] = ways
            return ways
        return decode(0)