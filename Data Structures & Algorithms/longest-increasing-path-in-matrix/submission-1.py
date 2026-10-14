class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = 0

        def dfs(r, c): 
            longest = 1
            if (r, c) in memo:
                return memo[(r, c)]
            for nr, nc in directions: 
                new_row = r + nr
                new_col = c + nc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and matrix[new_row][new_col] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(new_row, new_col))
                    memo[(r, c)] = longest

            return longest





        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c))
        
        return result


                        
        