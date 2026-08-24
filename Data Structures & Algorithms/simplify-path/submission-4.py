class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        lst=[]
        print(path)
        for x in path:
            if x == "..":
                if lst:
                    lst.pop()
            elif x == "" or x == ".":
                continue
            else:
                lst.append(x)
        z = "/"
        for x in range(len(lst)):
            z+=lst[x]
            if x != len(lst)-1:
                z+="/"
        return z
            