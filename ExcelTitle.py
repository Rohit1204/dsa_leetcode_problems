"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
Z -> 26
AA -> 27
AB -> 28 

"""
def convertToTitle(columnNumber: int) -> str:
    c=""
    while columnNumber:
        columnNumber,b = divmod(columnNumber-1,26)
        c+=chr(b +65)
    return c[::-1]