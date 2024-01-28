class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 1
        for i in range(1, n):
            output += 4*i
        return output