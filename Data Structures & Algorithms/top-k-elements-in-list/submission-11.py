class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countM = {}
        for num in nums:
            countM[num] = countM.get(num, 0) + 1

        heap = []

        for num, count in countM.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
        
