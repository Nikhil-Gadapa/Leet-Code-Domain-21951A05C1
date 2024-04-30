class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m={}
        pos=defaultdict(list)
        for i,val in enumerate(ring):
            pos[val].append(i)
        return self.help(0,0,pos,key,ring,m)
    def help(self,in_i,pos_v,pos,key,ring,m):
        if in_i==len(key):
            return 0
        if (in_i,pos_v) in m:
            return m[(in_i,pos_v)]
        ms=float('inf')
        for i in pos[key[in_i]]:
            if i>=pos_v:
                s=min(i-pos_v,pos_v+len(ring)-i)
            else:
                s=min(pos_v-i,i+len(ring)-pos_v)
            ms=min(ms,s+self.help(in_i+1,i,pos,key,ring,m))
        m[(in_i,pos_v)]=ms+1
        return ms+1

