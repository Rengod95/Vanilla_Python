import math
import time

n = int(input())
dp = [0] * (n+1)
dp[0], dp[1] = 0, 1

start =time.time()
for i in range(2,n+1):
    if int(math.sqrt(i))**2 == i:
        dp[i]=1
    else:
        dp[i] = i

for i in range(2,n+1):
    for j in range(1,int(math.sqrt(i))+1):
        dp[i] = min(dp[i],dp[j*j]+dp[i-j*j])

print(dp[n])
print(round(time.time()-start,3),"sec")


