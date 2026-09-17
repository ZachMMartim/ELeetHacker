class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        visited = set()

        def backtracking(index, path): 
            if index == len(nums):
                key = tuple(path)
                if key not in visited:
                    visited.add(tuple(path))
                    results.append(path.copy())
                return
            
            #include
            path.append(nums[index])
            backtracking(index + 1, path)
            path.pop()

            #exclude
            backtracking(index + 1, path)
        
        backtracking(0, [])
        return results

        