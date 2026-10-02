class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1Count = {}
        windowCount = {}

        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1

        left = 0

        for r in range(len(s2)):
            char = s2[r]
            windowCount[char] = windowCount.get(char, 0) + 1

            if (r - left) + 1 > len(s1):
                leftChar = s2[left]
                windowCount[leftChar] -= 1

                if windowCount[leftChar] == 0:
                    del windowCount[leftChar]
                left += 1
            
            if windowCount == s1Count:
                return True
            

        return False






        
        