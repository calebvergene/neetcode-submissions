class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [5, 10, 20]
        change = collections.defaultdict(int)

        for b in bills:
            if b == 5:
                change[5] += 1
            elif b == 10:
                if not change[5]: 
                    return False
                else: 
                    change[5] -= 1
                    change[10] += 1
            else:
                if not change[10]: 
                    return False
                else: 
                    change[10] -= 1
                if not change[5]: 
                    return False
                else: 
                    change[5] -= 1
                    change[20] += 1
        return True

    