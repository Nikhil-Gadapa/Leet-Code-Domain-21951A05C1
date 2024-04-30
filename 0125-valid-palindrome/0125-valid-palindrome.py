class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
            else:
                if s[i].isalnum():
                    j-=1
                else:
                    i+=1
        if i==j or i==j+1:
            return True
        return False