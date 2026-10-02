class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen, path = set(), []

        # list to track path. 
        # once find cycle, reverse and keep popping until you hit path[-1]

        def dfs(node):
            path.append(node)
            if node in seen: # should NEVER come across same node again. CYCLE
                return True
            
            seen.add(node)
            for neighbor in adj[node]:
                if len(path) > 1 and neighbor == path[-2]: # dont go backwards
                    continue
                cycle = dfs(neighbor)
                if cycle:
                    return True
                
            path.pop()

        
        dfs(1)

        # assumes we found cycle
        path.reverse()
        while path[0] != path[-1]:
            path.pop()
        
        pathset = set(path)
        print(pathset)
        for a, b in reversed(edges):
            if a in pathset and b in pathset:
                return [a,b]