class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        res=[0]*n
        count=[1]*n
        def func1(node,par):
            for i in d[node]:
                if i!=par:
                    func1(i,node)
                    count[node]+=count[i]
                    res[node]+=res[i]+count[i]
        def func2(node,par):
            for i in d[node]:
                if i!=par:
                    res[i]=res[node]-count[i]+n-count[i]
                    func2(i,node)
        func1(0,-1)
        func2(0,-1)
        return res