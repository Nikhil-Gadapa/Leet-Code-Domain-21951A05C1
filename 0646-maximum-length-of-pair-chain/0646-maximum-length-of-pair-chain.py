class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x:x[1])
        i=0
        count=0
        prev=pairs[0][0]-1
        
        while i<len(pairs):
            if pairs[i][0]>prev:
                count+=1
                prev=pairs[i][1]
            i+=1
        return count