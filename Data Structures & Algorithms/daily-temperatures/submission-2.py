class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # in a monotonic queue, store (temp, index)
        # if you get a new day thats hotter, keep popping and updating res
        result = [0] * len(temperatures)
        mono = []
        for i, temp in enumerate(temperatures):
            while mono and mono[-1][0] < temp:
                past_day = mono.pop()
                result[past_day[1]] = i - past_day[1]
            mono.append((temp, i))
        return result 
            
