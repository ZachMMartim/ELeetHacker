class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        #Empty subarray has a prefix of 0 and occurs once so far
        prefixSum = { 0 : 1}

        for n in nums:
            currSum += n
            diff = currSum - k

            res += prefixSum.get(diff, 0)
            #Increment the number of prefix sums that have this currSum value
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res

        