class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj = {}
        visited, seen = set(), set()

        # make adjacency list.
        for a,b in prerequisites:
            if b not in adj:
                adj[b] = []
            adj[b].append(a)

        # dfs. when a node is done, add to order stack. 
        def dfs(course):
            if course in seen:
                # we have a cycle
                return True
            elif course in visited:
                return False
            seen.add(course)

            cycle = False
            if course in adj: # course might not have dependencies
                for next_course in adj[course]:
                    cycle = cycle or dfs(next_course)
            
            order.append(course)
            visited.add(course)
            seen.remove(course)
            return cycle

        for course in range(numCourses):
            if dfs(course):
                return []

        # then return stack reversed 
        order.reverse()
        return order