def extendedEuclidean(a, b):
    if a == 0:
        gcd = b
        return 0, 1, gcd
    x1, y1, gcd = extendedEuclidean(b % a, a)
    x = y1 - (b//a)*x1
    y = x1
    return x, y, gcd


a = 57
b = 81
print(extendedEuclidean(a, b))


'''

Ans => (10, -7, 3)

'''
