class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #given piles where piles[i] is number of bananas in ith pile
        #h = num of hours to eat all bananas in a pile
        #k = bananas / hr rate

        #Each hour, choose a pile to eat k bananas. 
        #If pile has < k, finish the pile but you cannot eat from another pile 

        l = 1
        r = max(piles)

        res = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles: 
                time += math.ceil(pile / k)
            if time <= h:
                res = k
                r = k - 1
            else: 
                l = k + 1
        return res
        


        
        