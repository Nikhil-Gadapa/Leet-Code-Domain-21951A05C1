class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count={}
        for num in nums:
            count[num]= count.get(num,0)+1
        end={}
        for num in nums:
            if count[num]==0:
                continue
            #print(count)
            count[num]-=1
            
            if end.get(num-1,0)>0:
                end[num-1]-=1
                end[num]=end.get(num,0)+1
            elif count.get(num+1,0)>0 and count.get(num+2,0)>0:
                count[num+1]-=1
                count[num+2]-=1
                end[num+2]=end.get(num+2,0)+1
            else:
                return False
        return True
            
                