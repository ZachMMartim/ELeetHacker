class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())
                return
            
            #include
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            #exclude
            backtrack(i + 1, path)

        backtrack(0, [])
        return result
        
        