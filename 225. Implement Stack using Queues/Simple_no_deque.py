from collections import deque
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.last = Node(x, self.last)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.last.item
        self.last = self.last.next
        return x
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.last:
            return self.last.item
        else:
            return None        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.top() is None:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
