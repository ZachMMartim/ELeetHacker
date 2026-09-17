class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

        def bfs(startingCells):
            reached = set(startingCells)
            queue = deque(reached)

            while queue:
                row, col = queue.popleft()

                for rowChange, colChange in directions:
                    newRow = row + rowChange
                    newCol = col + colChange

                    if (0 <= newRow < rows and 0 <= newCol < cols and (newRow, newCol) not in reached and heights[newRow][newCol] >= heights[row][col]):
                        reached.add((newRow, newCol))
                        queue.append((newRow, newCol))

            return reached

        pacificStarts = []
        atlanticStarts = []

        for row in range(rows):
            pacificStarts.append((row, 0))
            atlanticStarts.append((row, cols - 1))

        for col in range(cols):
            pacificStarts.append((0, col))
            atlanticStarts.append((rows - 1, col))

        pacificReachable = bfs(pacificStarts)
        atlanticReachable = bfs(atlanticStarts)

        bothOceans = pacificReachable & atlanticReachable

        return [[row, col] for row, col in bothOceans]

        