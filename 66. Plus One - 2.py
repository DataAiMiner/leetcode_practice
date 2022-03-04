class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_to_num = int(''.join(digits))
        num_to_str = list(str(str_to_num + 1))
        
        return [int(num) for num in num_to_str]
        
