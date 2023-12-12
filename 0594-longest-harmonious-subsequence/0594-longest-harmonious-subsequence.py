class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_counts={}
        for num in nums:
            nums_counts[num]= nums_counts.get(num,0)+1
        max_lenght=0
        
        for num in nums_counts:
            if num+1 in nums_counts:
                max_lenght= max(max_lenght,nums_counts[num]+nums_counts[num+1])
        return max_lenght