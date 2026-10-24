class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        a = students.count(0)
        b = students.count(1)
        i = 0
        while i < len(sandwiches):
            if sandwiches[i] == 0 and a > 0:
                a -= 1
            elif sandwiches[i] == 1 and b > 0:
                b -= 1
            else:
                break
            i += 1
        return a + b