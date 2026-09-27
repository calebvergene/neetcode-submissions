class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        incar = []
        trips.sort(key=lambda c : c[1])

        for trip in trips:
            heapq.heappush(incar, (trip[2], trip[0])) # to, passengers
            capacity -= trip[0]
            while incar and incar[0][0] <= trip[1]: # drop them off
                _, passengers = heapq.heappop(incar)
                capacity += passengers
            if capacity < 0:
                return False

        return True


