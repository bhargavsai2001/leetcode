class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p=head
        res=p.next   
        while True:
            q=p.next  
            r=p.next.next    
            q.next=p   
            if not r or not r.next:
                p.next=r     
                break
            q.next.next=r.next
            p=r
    
        return res