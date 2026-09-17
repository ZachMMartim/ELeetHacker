class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ([[0, 1], [0, -1], [1, 0], [-1, 0]])
        visited = set()

        def dfs(row, col, i):
            if(row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[i]):
                return False
            if i == len(word) - 1: 
                return True
            
            visited.add((row, col))
            for row_change, col_change in directions: 
                new_row = row + row_change
                new_col = col + col_change
                if dfs(new_row, new_col, i + 1):
                    visited.remove((row, col))
                    return True
            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False




        
        



        