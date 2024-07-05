class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum=nums[0]
        m_sum=c_sum
        for n in nums[1:]:
            c_sum=max(n,c_sum+n)
            if c_sum>m_sum:
                m_sum=c_sum
        return m_sum

    