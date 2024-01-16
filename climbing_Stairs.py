"""
You are climbing a staircase.
It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
def climbStairs(n: int) -> int:
    if n<=3:
        return n
    current= 0
    prevprevious =1
    previous =2
    for i in range(3,n+1):
        current = previous + prevprevious
        prevprevious = previous
        previous =current
    return current