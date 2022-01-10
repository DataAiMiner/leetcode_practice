import numpy as np

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        matrix = np.array(matrix)
        for i in range(n):
            for j in range(n):
                if (i+1) not in matrix[j]:
                    return False
                if (i+1) not in matrix[:,j]:
                    return False
        return True
