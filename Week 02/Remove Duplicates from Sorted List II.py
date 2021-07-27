class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = defaultdict(int)
        temp = head
        ans = ListNode()
        res = ans
        while temp:
            d[temp.val] += 1
            temp = temp.next
        for i in d.keys():
            if d[i]==1:
                ans.next = ListNode(i)
                ans = ans.next
        return res.next