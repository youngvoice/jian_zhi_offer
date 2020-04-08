class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i, j = 0, n - 1
        

        while i < m and j > -1:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                pass
        return False