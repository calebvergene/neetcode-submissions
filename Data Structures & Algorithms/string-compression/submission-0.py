class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0
        prev = None
        count = 0
        for c in chars:
            if c == prev:
                count += 1
                continue
            else:
                chars[k] = c
                k += 1
                if count > 1:
                    for i in str(count):
                        chars[k] = i
                        k += 1
                prev = c
                count = 1
        
        if count > 1:
            for i in str(count):
                chars[k] = i
                k += 1
        return k
            
