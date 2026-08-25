class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        dct = defaultdict(list)
        for x, y in edges:
            dct[x].append(y)
            dct[y].append(x)
        
        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return False
            visited.add(curr)
            for x in dct[curr]:
                if x == parent:
                    continue
                if not dfs(x, curr):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n