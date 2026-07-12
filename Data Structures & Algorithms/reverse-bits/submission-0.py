class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0 
        for _ in range(31):
            # see if there is a one at the end of n
            bit = 1 & n
            r |= bit
            r = r << 1
            # move n to the next bit
            n = n >> 1
        return r