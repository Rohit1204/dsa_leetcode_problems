"""
find square root without using any build in function
"""
import math
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    a = x/2
    for i in range(100):
        a = 0.5 * (a +x/a)

    return math.floor(a)