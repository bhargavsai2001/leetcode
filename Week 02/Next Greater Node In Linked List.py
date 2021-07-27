class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        itr = head

        stack = [[0,itr.val]]

        itr = itr.next

        ans = [0] * 10000

        ind = 1

        while itr:

            if stack and stack[-1][1] > itr.val:

                stack.append([ind, itr.val])

                ind += 1

                itr = itr.next

            else:

                while stack and stack[-1][1] < itr.val:

                    ans[stack.pop()[0]] = itr.val

                stack.append([ind,itr.val])

                ind += 1

                itr = itr.next

        return ans[:ind]