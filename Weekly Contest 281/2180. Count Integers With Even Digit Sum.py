class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        i= 0
        for i in range (1, num+1):
            digit_sum = 0
            copy_i = i
            while copy_i:
                digit_sum += copy_i % 10
                copy_i //= 10
            if digit_sum % 2 == 0:
                count += 1
        
        return count
