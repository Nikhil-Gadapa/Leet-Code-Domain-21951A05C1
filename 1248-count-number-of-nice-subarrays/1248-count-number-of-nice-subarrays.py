class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
            count=0
            left=0
            current_odd_count=0
            prefix_count=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    current_odd_count+=1
                    prefix_count=0
                while current_odd_count==k:
                    if nums[left]%2==1:
                        current_odd_count-=1
                    prefix_count+=1
                    left+=1
                count+=prefix_count
            return count