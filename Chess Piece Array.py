def message():
    print("Enter a value ")

def isqrt(n):
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    x = '{0:.3g}'.format(x)
    return x

message()
a = int(input())
message()
b = int(input())

c = b**2+a**2

print("The Hypotenues is", isqrt(c))