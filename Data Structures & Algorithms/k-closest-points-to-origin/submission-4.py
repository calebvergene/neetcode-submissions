class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def distance_origin(x, y):
            return math.sqrt(x**2+y**2)
        
        for point in points:
            distance = distance_origin(point[0], point[1])
            heapq.heappush(heap, (-distance, point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[point[1], point[2]] for point in heap]