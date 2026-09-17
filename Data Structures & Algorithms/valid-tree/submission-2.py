class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])        
            adj[edge[1]].append(edge[0])

        visited = set()

        def check_cycle(node, path, prev):
            nonlocal visited
            if node in visited:
                return False
            if node in path:
                return True
            
            path.add(node)
            cycle = False
            for neighbor in adj[node]:
                # cannot dfs to prev node 
                if neighbor != prev:
                    cycle = cycle or check_cycle(neighbor, path, node)
            path.remove(node)
            visited.add(node)

            return cycle
        
        if check_cycle(0, set(), None):
            return False
        return len(visited) == n
            

                    

