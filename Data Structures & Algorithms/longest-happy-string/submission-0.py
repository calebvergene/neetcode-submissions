class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # a=3, b=0, c=1
        # c aa 
        # a c aa

        # start with the char with the highest freq
        # a=6, c=2 
        # last_letter, count (reset if last_letter different)
        # (-4, a) (-2, a)
        # aa cc aa
        # aa c aa c aa

        # count tracker for last two used letters to know when to go on cooldown 
        # when a character is on cooldown, do not have in the heap. 


        heap = []
        happy = ""
        last_letter, count, cooldown = "", 0, None

        # initialize the heap (-freq, letter)
        letters = {'a':a, 'b':b, 'c':c}
        for letter in letters:
            if letters[letter]:
                heapq.heappush(heap, [-letters[letter], letter])

        while heap:
            freq, letter = heapq.heappop(heap)
            if letter == last_letter:
                count += 1
                if count == 3:
                    cooldown = [freq, letter]
                    continue
            else:
                last_letter = letter
                count = 1

            # now add back to heap 
            freq += 1
            happy += letter
            if freq < 0:
                heapq.heappush(heap, [freq, letter])
        
            
            if cooldown:
                heapq.heappush(heap, cooldown)
                cooldown = None
        
        return happy
