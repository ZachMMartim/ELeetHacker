class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def BFS(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = "0"
            while queue: 
                currRow, currCol = queue.popleft()
                for row_change, col_change in directions: 
                    nr = currRow + row_change
                    nc = currCol + col_change
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1": 
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    numOfIslands += 1
                    BFS(i, j)
        return numOfIslands


        
        