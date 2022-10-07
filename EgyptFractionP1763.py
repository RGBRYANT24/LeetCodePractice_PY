def gcd(a, b):
    if a < b:
        a, b = b, a
    while(b > 0):
        a, b = b, a%b
    return a

def yf(a: int, b: int):
    tmp = gcd(a, b)
    