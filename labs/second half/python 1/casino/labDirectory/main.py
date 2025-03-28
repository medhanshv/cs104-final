# '''
#     Let's go to casino
#     Author: Saksham Rathi
# '''
# import sys
# n=int(sys.argv[1])
# N=1000000007
# memo=dict()
# sys.setrecursionlimit(10**6)

# def f(n):
#     if(n<=0):
#         memo[n]=0
#         return 0
#     if(n==1):
#         memo[n]=1
#         return 1
#     if(n==2):
#         memo[n]=2
#         return 2
#     if(n in memo):
#         return memo[n]
#     elif(n<=6):
#         ans=(1+f(n-1)+f(n-2)+f(n-3)+f(n-4)+f(n-5)+f(n-6))%N
#         memo[n]=ans
#         return ans
#     else:
#         ans = (f(n-1) % N + f(n-2) % N + f(n-3) % N + f(n-4) % N + f(n-5) % N + f(n-6) % N) % N
#         memo[n]=ans
#         return ans
  
# print(f(n))



import sys

n = int(sys.argv[1])
N = 10**9 + 7  
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(1, 7): 
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % N

print(dp[n])
