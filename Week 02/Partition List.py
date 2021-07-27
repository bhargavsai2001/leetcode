class Solution(object):
    def partition(self, head, x):
        if (head is None or head.next is None):
            return head
    
        else:
            smaller=ListNode("Dummy")
            pind=smaller

            larger=ListNode("Dummy")
            pind2=larger

            temp=head

            while temp:
                if temp.val < x:
                    pind.next=temp
                    pind=pind.next
                else:
                    pind2.next=temp
                    pind2=pind2.next
                temp=temp.next
            pind2.next=None

            pind.next=larger.next

            return smaller.next