class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = deque()

        # Put ALL treasures into the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))