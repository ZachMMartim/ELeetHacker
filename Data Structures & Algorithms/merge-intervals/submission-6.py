class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals: 
            currentEnd = result[-1][1]
            if start <= currentEnd: 
                result[-1][1] = max(currentEnd, end)
            else: 
                result.append([start, end])
        

        return result
            

        