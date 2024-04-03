class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        print(properties)
        max_defence=0
        weak_count=0
        for a,d in properties:
            if d<max_defence:
                weak_count+=1
            else:
                max_defence=d
                
        return weak_count