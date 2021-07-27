class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.M = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        update = [newValue]*(col2-col1+1)
        for r in range(row1,row2+1):
            self.M[r][col1:col2+1] = update
            
    def getValue(self, row: int, col: int) -> int:
        return self.M[row][col]