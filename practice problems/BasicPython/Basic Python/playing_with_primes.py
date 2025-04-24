import numpy as np
import math
import time


n=int(input())
arr=np.zeros(n,dtype=int)
for i in range(n):
    arr[i]=int(input())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
start_time = time.time()

m=np.max(arr)

ans=np.zeros(m+1,dtype=int)
i=0
j=0
while(ans[-1]==0):
    if(is_prime(i)):
        ans[j]=i
        j+=1
        if(is_prime(i-2)):
            ans[j]=i
            j+=1
    i+=1
for x in arr:
    print(ans[x-1])
print("--- %s ms ---" % (1000*(time.time() - start_time)))