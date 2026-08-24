class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory=""
        for char in path:
            if directory and char == "/":
                if (directory == "."): ##ignore single period
                    directory = ""
                    continue
                elif (directory == ".."): # pop the top of the stack, go back a directory
                    if stack:
                        stack.pop()
                    directory=""
                    continue
                else: ##mean you should have a valid directory, add it 
                    stack.append(directory) 
                    directory=""
                    continue
            else: ## either directory is empty or not looking at / 
                if (char == "/"):
                    continue
                directory += char
        if (directory == ".."):
            stack.pop()
        elif(directory and directory != "."):
            stack.append(directory)
        finalString="/"
        for x in stack:
            finalString += x
            finalString += "/"
        if (len(finalString) == 1):
            return finalString
        return finalString[:-1]

                
                
                
                
            
             
            