from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]
        
        
        for v1, v2 in edges:
            graph[v2].append(v1)
        
        
        ancestors = [set() for _ in range(n)]
        
        
        for start in range(n):
            stack = [start]
            visited = set()
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in ancestors[start]:
                        ancestors[start].add(neighbor)
                        stack.append(neighbor)
                    ancestors[start].update(ancestors[neighbor])
        
        
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result
