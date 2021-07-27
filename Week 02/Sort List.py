class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        current = head
        result = []
        result_h = ListNode()
        result_tail = result_h
        while current:
            result.append(current.val)
            current = current.next
        result.sort()            
        for i in range(len(result)):
            result_tail.next = ListNode(result[i])
            result_tail = result_tail.next
        return result_h.next