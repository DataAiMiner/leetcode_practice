class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        if len(asteroids) == 1:
            if mass < asteroids[0]:
                return False
            else:
                return True
        
        ast_sorted = sorted(asteroids)
        
        summation = mass
        for i in range(len(ast_sorted)):
            print(ast_sorted[i])
            if summation >= ast_sorted[i]:
                summation += ast_sorted[i]
            else:
                return False
        
        return True
