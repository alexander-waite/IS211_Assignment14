def rf(n):
    if n <= 1:
        return n
    else:
        return rf(n - 1) + rf(n - 2)


def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    elif b == 0:
        return a
    if a < b:
        r = b % a
        return gcd(a, r)
    elif a > b:
        r = a % b
        return gcd(b, r)


# print(gcd(1701, 3768))


def compareTo(s1, s2):
    if len(s1) == len(s2) and len(s1) is 0:
        return 0
    s1 = s1[0:(len(s1) - 1)]
    ss1 = len(s1)
    s2 = s2[0:(len(s2) - 1)]
    ss2 = len(s2)
    if ss1 == 0:
        return -1
    elif ss2 == 0:
        return 1
    else:
        return compareTo(s1, s2)
