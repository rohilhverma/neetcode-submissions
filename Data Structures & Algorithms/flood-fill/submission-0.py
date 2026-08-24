class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.startingColor=image[sr][sc]
        if self.startingColor == color:
            return image
        def help(row, col):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != self.startingColor:
                return 
            
            image[row][col] = color
            help(row+1,col)
            help(row-1,col)
            help(row,col+1)
            help(row,col-1)
            return


        help(sr,sc)
        return image