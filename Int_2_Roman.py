"""
Convert integer to roman
"""
def intToRoman(num: int) -> str:
    number = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
    "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    a=""
    while num:
        div = num // number[i]
        num %= number[i]

        while div:
            a+=sym[i]
            div -= 1
        i -= 1

    return a