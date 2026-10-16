class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for word in strs: 
            strMap[''.join(sorted(word))].append(word)
        
        return list(strMap.values())
            
        

        