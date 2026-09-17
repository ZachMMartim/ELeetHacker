class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        usedElement = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if usedElement[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not usedElement[i - 1]:
                    continue
                usedElement[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                usedElement[i] = False


        backtrack([])
        return result
        