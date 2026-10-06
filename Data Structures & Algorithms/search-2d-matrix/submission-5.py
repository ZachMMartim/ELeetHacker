class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        botRow = ROWS - 1
        topRow = 0

        while topRow <= botRow:
            midRow = (botRow + topRow) // 2
            if matrix[midRow][-1] < target:
                topRow = midRow + 1
            elif matrix[midRow][0] > target:
                botRow = midRow - 1
            else:
                break

        left = 0
        right = COLS - 1
        if not (topRow <= botRow):
            return False
        midRow = (botRow + topRow) // 2
        while left <= right: 
            mid = (left + right) // 2
            if matrix[midRow][mid] < target: 
                left = mid + 1
            elif matrix[midRow][mid] > target:
                right = mid - 1
            elif matrix[midRow][mid] == target:
                return True
        
        return False
                