class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dct=defaultdict(list)

        for x, y in prerequisites:
            dct[x].append(y)
        visited=set()
        def dfs(curr, visited):
            temp=True
            if curr in visited:
                return False
            visited.add(curr)
            for n in dct[curr]:
                temp = temp & dfs(n, visited)
                if not temp:
                    return False
            visited.remove(curr)
            dct[curr]=[]
            return True
        z = True
        for x, y in prerequisites:
            z = z & dfs(x, visited)
        return z

