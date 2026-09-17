class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                #implicit exclude
                if nums[i] in path:
                    continue

                #include
                path.append(nums[i])
                backtrack(path)
                path.pop()
                

        
        backtrack([])
        return result
        