class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            if index == len(nums): 
                result.append(path.copy())
                return
            
            #include
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            #exclude
            backtrack(index + 1, path)


        backtrack(0, [])
        return result
        
        