"""
Given two binary strings a and b, 
return their sum as a binary string.
"""
def addBinary(a: str, b: str) -> str:
    a = int(a,2)
    b= int(b,2)
    return bin(a + b)[2:]