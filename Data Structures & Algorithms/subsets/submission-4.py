class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path, i):
            if i >= len(nums):
                result.append(path.copy())
                return
            
            #include
            path.append(nums[i])
            dfs(path, i + 1)
            path.pop()

            #exclude
            dfs(path, i + 1)
        
        dfs([], 0)
        return result
        