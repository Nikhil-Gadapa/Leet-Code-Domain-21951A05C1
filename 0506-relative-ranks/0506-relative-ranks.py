class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d=defaultdict(int)
        place=["Gold Medal", "Silver Medal", "Bronze Medal"]
        n=len(score)
        a=[""]*n
        for i in range(n): d[score[i]]=i
        score.sort(reverse=True)
        for i in range(n):
            if i<3:
                a[d[score[i]]]= place[i]
            else:
                a[d[score[i]]]= str(i+1)
        return a