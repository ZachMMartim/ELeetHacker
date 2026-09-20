class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c): 
            if (r, c) in memo:
                return memo[(r, c)]
            longest = 1
            for row_change, col_change in directions: 
                nr = r + row_change
                nc = c + col_change
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))
            memo[(r, c)] = longest
            return memo[(r, c)]
        
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                answer = max(answer, dfs(r, c))
        return answer
            

                        
        