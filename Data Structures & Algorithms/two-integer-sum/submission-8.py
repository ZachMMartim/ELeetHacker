class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in compMap:
                return [compMap[complement], i]
            compMap[num] = i

                    