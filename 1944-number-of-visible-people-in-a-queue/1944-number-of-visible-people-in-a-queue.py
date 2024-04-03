class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack=[]
        res=[1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count=0
            while stack and heights[stack[-1]]<heights[i]:
                stack.pop()
                count+=1
            if stack:
                res[i]+=count
            else:
                res[i]=count
            stack.append(i)
        return res