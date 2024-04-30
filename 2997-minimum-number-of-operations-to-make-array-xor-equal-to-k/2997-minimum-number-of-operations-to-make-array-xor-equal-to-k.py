class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        fx=0
        for i in nums:
            fx^=i
        count=0
        while fx or k:
            if (fx%2)!=(k%2):
                count+=1
            k//=2
            fx//=2
        return count