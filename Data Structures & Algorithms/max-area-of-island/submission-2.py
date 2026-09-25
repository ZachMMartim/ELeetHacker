class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maxArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def BFS(row, col, currentArea):
            nonlocal maxArea
            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0

            while queue: 
                currRow, currCol = queue.popleft()
                currentArea += 1
                maxArea = max(maxArea, currentArea)
                for row_change, col_change in directions:
                    nr = currRow + row_change
                    nc = currCol + col_change
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1: 
                        queue.append((nr, nc))
                        grid[nr][nc] = 0


        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    BFS(i, j, 0)

        return maxArea
        