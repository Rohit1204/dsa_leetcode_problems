"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def multiply(num1: str, num2: str) -> str:
    from itertools import zip_longest
    a=b=0
    for i,j in zip_longest(num1, num2, fillvalue=''):
        a = a * 10 + (ord(i)-48) if i!='' else a
        b=  b * 10 + (ord(j)-48) if j!='' else b
    
    return str(a * b)