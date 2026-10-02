class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tFreq = {}
        windowFreq = {}

        for char in t: 
            tFreq[char] = tFreq.get(char, 0) + 1
        
        windowChars, tChars = 0, len(tFreq)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for r in range(len(s)):
            char = s[r]
            windowFreq[char] = windowFreq.get(char, 0) + 1

            if char in tFreq and windowFreq[char] == tFreq[char]:
                windowChars += 1
            while windowChars == tChars:
                if (r - left) + 1 < resLen:
                    res = [left, r]
                    resLen = (r - left) + 1
                windowFreq[s[left]] -= 1
                if s[left] in tFreq and windowFreq[s[left]] < tFreq[s[left]]:
                    windowChars -= 1
                left += 1
        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""

        