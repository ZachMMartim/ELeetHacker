class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        path = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visitedCell = set()
        visitedCols = []
        visitedRows = []
        def BFS(row, col):
            path.append((row, col))
            visitedCols.clear()
            visitedRows.clear()
            visitedCell.clear()
            while path:
                currRow, currCol = path.popleft()
                visitedCols.append(currCol)
                visitedRows.append(currRow)
                visitedCell.add((currRow, currCol))
                for row_change, col_change in directions: 
                    new_row, new_col = currRow + row_change, currCol + col_change
                    if 0 <= new_row < len(heights) and 0 <= new_col < len(heights[0]) and heights[new_row][new_col] <= heights[currRow][currCol] and (new_row, new_col) not in visitedCell:          
                        path.append((new_row, new_col))

            
            reachesAtlantic = (len(heights) - 1 in visitedRows or len(heights[0]) - 1 in visitedCols)
            reachesPacific = (0 in visitedRows or 0 in visitedCols)
            return reachesAtlantic and reachesPacific
                        
                        



        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if BFS(i, j): 
                    result.append([i, j])
        return result

        