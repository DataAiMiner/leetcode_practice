class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = { ')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if len(stack) == 0 or dictionary[char] != stack.pop():
                    return False
        return len(stack) == 0
