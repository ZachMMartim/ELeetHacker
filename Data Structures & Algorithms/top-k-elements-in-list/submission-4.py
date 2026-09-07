class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num, count in count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [num for count, num in heap]

        


        
        