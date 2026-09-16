class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                row, col = queue.popleft()
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1"):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = "0"


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    numOfIslands += 1
                    bfs(row, col)
            

        return numOfIslands




        

        