class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # order the positions and speeds list 
        # then, in sam eorder, make a list of the time that they will reach target 
        # think of it like a stack where larger number pops smaller nums below.

        for i, car in enumerate(position):
            position[i] = (car, speed[i])
        position.sort()
        
        for i, tup in enumerate(position):
            pos, speed = tup
            distance = target - pos
            hours = distance / speed
            position[i] = hours
        
        fleets = 1
        ahead = position[-1]
        for i in range(len(position)-1, -1, -1):
            # if car is slower, new fleet + new ahead car
            if position[i] > ahead:
                fleets += 1
                ahead = position[i]
        
        return fleets
