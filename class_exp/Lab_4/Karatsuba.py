def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    p = len(str(x))
    q = len(str(y))
    n = max(p, q)
    mid = n // 2
    B = x % (10 ** (n // 2))
    A = x // (10 ** (n // 2))
    D = y % (10 ** (n // 2))
    C = y // (10 ** (n // 2))
    ac = karatsuba(A, C)
    bd = karatsuba(B, D)
    abcd = karatsuba(A + B, C + D)
    middle_term = abcd - ac - bd
    return (ac * 10 ** (2 * mid)) + (middle_term * 10 ** mid) + bd
    #return (ac*10**n + bd + abcd *10 ** n//2)

x = 55618
y = 1565
print(karatsuba(x,y))
print (x*y)