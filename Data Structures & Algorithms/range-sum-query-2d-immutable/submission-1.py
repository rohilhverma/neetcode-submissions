class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        col=len(matrix[0])
        c=[[0 for _ in range(col+1)] for _ in range(rows+1)]
        for x in range(rows):
            prefix=0
            for y in range(col):
                prefix+=matrix[x][y]
                above=c[x][y+1]
                c[x+1][y+1]=above+prefix
        self.c=c
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a,b,x,y=row1+1,col1+1,row2+1,col2+1

        return self.c[x][y] - self.c[x][b-1] - self.c[a-1][y] + self.c[a-1][b-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)