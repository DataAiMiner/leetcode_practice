from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_list = list(s)
        stack = deque(s)
        while len(stack) > 0:
            print(stack.pop())
            print(stack.popleft())
