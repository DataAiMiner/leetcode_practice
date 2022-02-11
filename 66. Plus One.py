class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_to_num = int(''.join([str(digit) for digit in digits]))
        return [int(char) for char in str(digit_to_num+1)]
