class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        leftover = num % 3
        if leftover == 0:
            return [num//3 - 1, num//3, num//3 + 1]
        else:
            return []
        
