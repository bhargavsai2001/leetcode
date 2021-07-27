class Solution:
	def flatten(self, head: 'Node') -> 'Node':
		a=self.dfs(head,[])
		if a:
			N=Node(a[0])
			x=N
			for i in range(1,len(a)):
				p=Node(a[i])
				p.prev=N
				N.next=p
				N=p
			return(x)    
		else:
			return(head)
	def dfs(self,x,a):
		if x is None:
			return
		a.append(x.val)
		if x.child:
			self.dfs(x.child,a)
		self.dfs(x.next,a)
		return(a)