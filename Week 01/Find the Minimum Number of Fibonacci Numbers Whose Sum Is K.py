class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        fibo = [0,1]
        i= 2
        while fibo[i-1] < k:
            
            fibo.append(fibo[i-1]+fibo[i-2])
            i+=1
        
        count = 0
        ind = len(fibo)-1
        while k != 0 :
            result = k-fibo[ind]
            if result >0 :
                count+=1
                k = result
            elif result == 0:
                return count+1
            else:
                ind-=1
        return count