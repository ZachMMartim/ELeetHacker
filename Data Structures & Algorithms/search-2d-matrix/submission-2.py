class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        topR, botR = 0, ROWS - 1
        while topR <= botR:
            midRow = (botR + topR) // 2
            if target > matrix[midRow][-1]:
                topR = midRow + 1
            elif target < matrix[midRow][0]:
                botR = midRow - 1
            else: 
                break

        if not (topR <= botR):
            return False
        row = (topR + botR) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (r + l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
                