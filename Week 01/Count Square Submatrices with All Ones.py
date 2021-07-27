class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        s=0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if i==0 or j==0:
                    s+=matrix[i][j]
                    
                elif matrix[i][j]==1:
                    matrix[i][j]=min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
                    s+=matrix[i][j]
                    
        return s