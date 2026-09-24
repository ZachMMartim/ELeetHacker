class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

        