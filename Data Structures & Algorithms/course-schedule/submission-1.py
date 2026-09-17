class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency graph 
        prereqs = defaultdict(list)
        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])
        
        visited = set()
        
        def check_cycle(course, path):
            nonlocal visited
            if course in visited:
                return False

            if course in path:
                return True
            
            path.add(course)
            cycle = False
            
            for prereq in prereqs[course]:
                cycle = cycle or check_cycle(prereq, path)
            
            path.remove(course)
            visited.add(course)
            return cycle
            

        for course in range(numCourses):
            if check_cycle(course, set()):
                return False
        return True


