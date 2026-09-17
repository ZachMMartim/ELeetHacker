
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        freshFruit = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rottenCells = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruit += 1
                if grid[i][j] == 2:
                    rottenCells.append([i, j])

        while rottenCells and freshFruit > 0:
            numOfCurrRotCells = len(rottenCells)
            for i in range(numOfCurrRotCells):
                currRotRow, currRotCol = rottenCells.popleft()
                for row_change, col_change in directions:
                    new_row = row_change + currRotRow
                    new_col = col_change + currRotCol
                    if(0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1):
                        rottenCells.append([new_row, new_col])
                        grid[new_row][new_col] = 2
                        freshFruit -= 1
            minutes += 1
        return minutes if freshFruit == 0 else -1
            

                


        
                






        