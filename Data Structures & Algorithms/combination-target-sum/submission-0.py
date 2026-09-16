class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if sum(path) == target:
                result.append(path.copy())
                return
            if sum(path) > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        
        backtrack(0, [])
        return result
        
        