class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        #go over cars in reverse order, starting from the car in the furthest ahead position
        for p, s in sorted(pair)[::-1]: 
            #Grab the time it takes for the current car to reach destination
            stack.append((target - p) / s)
            #if the car behind another car has a shorter time to reach destination, then they join the same fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        