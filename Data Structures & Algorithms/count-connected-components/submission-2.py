class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited, component = set(), set()
        total = 0

        def dfs(node):
            nonlocal component
            component.add(node)
            for neighbor in adj[node]:
                if neighbor not in component:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                total += 1
                visited = visited | component
                component = set()

        return total 