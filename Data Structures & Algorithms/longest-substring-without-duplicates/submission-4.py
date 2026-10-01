class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSub = set()
        left, right, longest = 0, 0, 0
        for char in s: 
            while char in currSub:
                currSub.remove(s[left])
                left += 1
            right += 1
            currSub.add(char)
            longest = max(longest, (right - left))

        return longest
            