class Solution:
    def binary_search(self, row, target):
        left, right = 0, len(row) - 1
        while left <= right:
            m = left + (right - left)
            if row[m] == target:
                return True
            elif row[m] < target: #search right
                left = m + 1
            else: #search left
                right = m - 1
        return False




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Intuition:
        - since we need a log(m * n) solution,
        we should go through each row of the matrix
        and run binary search
        '''
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False