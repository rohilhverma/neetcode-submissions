class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst =[]
        for x in range(len(operations)):
            if (operations[x] == "+"):
                lst.append(int(lst[-1]) + int(lst[-2]))
            elif (operations[x] == "C"):
                lst.pop()
            elif (operations[x] == 'D'):
                lst.append(2 * int(lst[-1]))
            else:
                lst.append(int(operations[x]))
        return sum(lst)