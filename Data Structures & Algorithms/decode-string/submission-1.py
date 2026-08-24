class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        number =""
        for x in s: 
            if x != "]":
                stack.append(x)
            else:
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop() # removes parenthesis [
                while stack and stack[-1].isnumeric():
                    number = stack.pop() + number
                number = int(number)
                string *= number
                stack.append(string)
                string = ""
                number=""
        return "".join(stack)
