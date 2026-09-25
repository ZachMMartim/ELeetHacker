class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0


        def BFS(row, col): 
            queue = deque()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            grid[row][col] = "0"
            queue.append((row, col))
            while queue:
                currRow, currCol = queue.popleft()
                for row_change, col_change in directions:
                    newRow = currRow + row_change
                    newCol = currCol + col_change
                    if (0 <= newRow < len(grid)) and (0 <= newCol < len(grid[0])) and (grid[newRow][newCol] == "1"):
                        grid[newRow][newCol] = "0"
                        queue.append((newRow, newCol))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": 
                    numOfIslands += 1
                    BFS(i, j)
        return numOfIslands


        
        