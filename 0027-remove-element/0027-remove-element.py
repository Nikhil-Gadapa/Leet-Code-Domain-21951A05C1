class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        insert_index=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[insert_index]=nums[i]
                insert_index+=1
        
        return insert_index