class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        sum1=int((n*(n+1))/2)
        sum2=0
        for i in nums:
            sum2+=i
        return(sum1-sum2)
        