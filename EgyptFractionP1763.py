def gcd(a, b):
    if a < b:
        a, b = b, a
    while(b > 0):
        a, b = b, a%b
    return a

def yf(a: int, b: int):
    tmp = gcd(a, b)
    return a/tmp, b/tmp

def sum_num(num1 : tuple, num2 : tuple):
    result = (0 ,0)
    result[0] = num1[0] + num2[0]
    result[1] = num1[1] + num2[1]
    tmp = gcd(result[0], result[1])
    