# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        lenght=1
        curr=head
        while curr.next:
            curr=curr.next
            lenght+=1
        curr.next=head
        k%=lenght
        
        rotate=lenght-k
        while rotate:
            curr=curr.next
            rotate-=1
        head=curr.next
        curr.next=None
        return head