class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            if len(strs)<2:
                return strs[0]
            strs.sort()
            common_prefix=""
            i=0
            while i<len(strs[0]) and i<len(strs[-1]):
                if strs[0][i]==strs[-1][i]:
                    common_prefix+=strs[0][i]
                    i+=1
                else:
                    break
            return common_prefix