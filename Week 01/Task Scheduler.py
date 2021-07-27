class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:

    maps={}

    for task in tasks:

        maps[task]=maps.get(task,0)+1

    heap=[]

    count=0

    

    for key in maps:

        heapq.heappush(heap,-maps[key])

    while len(heap)>0:

        temp=[]

        while len(heap)>0 and len(temp)<n+1:

            temp.append(-heapq.heappop(heap))  

        lenTemp=len(temp)

        maxTemp=max(temp)

        if lenTemp==n+1 or maxTemp>1:

            count+=n+1

        else:

            count+=lenTemp

        if maxTemp>=1:

            for element in temp:

                if element>1:

                    heapq.heappush(heap,-element+1)

    return count