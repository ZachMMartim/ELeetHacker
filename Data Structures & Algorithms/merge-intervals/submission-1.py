class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
    
        for i, (start, end) in enumerate(intervals):
            previousEnd = result[-1][1]
            if start <= previousEnd:
                result[-1][1] = max(previousEnd, end)
            else: 
                result.append([start, end])
            
        return result

            

        