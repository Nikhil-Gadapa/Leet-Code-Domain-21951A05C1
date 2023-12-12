class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalAlice=sum(aliceSizes)
        totalBob=sum(bobSizes)
        
        targetTotal=(totalAlice+totalBob)//2
        
        for aliceCandy in aliceSizes:
            bobCandy= aliceCandy+ (targetTotal-totalAlice)
            if bobCandy in bobSizes:
                return[aliceCandy, bobCandy]
            