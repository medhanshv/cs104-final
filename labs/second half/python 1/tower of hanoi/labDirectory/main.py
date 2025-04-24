'''
    Tower of Hanoi
    Author: Abhi Jain
'''

'''
Write your code to solve tower of hanoi problem here
Take input from user for number of disks

Output format:
line 1: number of moves(N)
line 2: move1
line 3: move2
...
line N+1: moveN
'''

'''
To solve this problem, you can use the recursive approach.
'''

import argparse
n = argparse.ArgumentParser()
n.add_argument("n", type=int)
args = n.parse_args()
n = args.n
print(2**n-1)

a=1
b=2
c=3

def move(n):
    global a,b,c
    if(n==1):
        print(a,c)
    else:
        b,c=c,b
        move(n-1)
        b,c=c,b
        print(a,c)
        a,b=b,a
        move(n-1)
        a,b=b,a
move(n)