class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        visited = set()
        def backtrack(i, path):
            if len(path) == k:
                result.append(path.copy())
                return
        
            for i in range(i, n + 1):
                path.append(i)    
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result

        