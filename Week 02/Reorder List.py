class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        arr=[]
        cur = head
        i=0  
        while cur : 
            arr.append(cur.val)  
            cur = cur.next 
 
        for i in range(len(arr))  :
            if i % 2 == 1 :  
                popval =  arr.pop() 
                arr.insert(i, popval) 
        
        node = head 
        for i  in range(1, len(arr)) :
            node.next =  ListNode(arr[i]) 
            node= node.next 