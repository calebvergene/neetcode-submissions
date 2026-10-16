class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # basically detect if there is a cycle 
        adj = defaultdict(list)
        for a, b in prerequisites: # prereq -> class
            adj[b].append(a)
        
        explored, path = set(), set()
        def cycle(course):
            if course in path:
                return True
            
            path.add(course)
            cycle_detected = False
            for after in adj[course]:
                if after not in explored:
                    cycle_detected = cycle_detected or cycle(after)


            path.remove(course)
            explored.add(course)
            
            return cycle_detected
        
        for course in range(numCourses):
            if course not in explored:
                if cycle(course):
                    return False
        
        return True