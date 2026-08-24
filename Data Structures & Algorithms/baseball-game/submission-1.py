class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        for x in operations:
            if x == "+":
                lst.append(lst[-1]+lst[-2])
            elif x == "D":
                lst.append(lst[-1]* 2)
            elif x == "C":
                lst.pop()
            else:
                lst.append(int(x))
            print(lst)
        return sum(lst)