from collections import deque
class MyStack(object):

    def __init__(self):
        self.s = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.s) - 1):
            self.s.append(self.s.popleft())
        return self.s.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.s) - 1):
            self.s.append(self.s.popleft())
        a = self.s.popleft()
        self.s.append(a)
        return a

    def empty(self):
        """
        :rtype: bool
        """
        if self.s:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()