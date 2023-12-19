class Solution:
    def maximumSwap(self, num: int) -> int:
        list_num=[x for x in str(num)]
        print(list_num)
        p1,p2=0,0
        max_digit=len(list_num)-1
        
        for i in range(len(list_num)-1,-1,-1):
            if list_num[i]>list_num[max_digit]:
                max_digit=i
            elif list_num[i]<list_num[max_digit]:
                p1,p2=i, max_digit
        list_num[p1],list_num[p2]=list_num[p2],list_num[p1]
        return int("".join(list_num))