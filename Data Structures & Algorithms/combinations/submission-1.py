class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(i, path):
            if i > n:
                if len(path) == k:
                    result.append(path.copy())
                return
            
            #include
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

            #exclude
            backtrack(i + 1, path)
        backtrack(1, [])
        return result
            
            
            