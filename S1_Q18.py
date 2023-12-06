# a > b > c > d > e
min = int()
for b in range(2,10000):
    print(b)
    for a in range(b + 1,10000):
        if a > b:
            if (a*b) % (2*a-b) == 0 and (a*b) % (3*a-2*b) == 0 and (a*b) % (4*a-3*b) == 0:
                c = (a*b) // (2*a-b)
                if b > c and b - a == c - b:
                    d = (a*b) // (3*a-2*b)
                    if c > d and d - c == c - b:
                        e = (a*b) // (4*a - 3*b)
                        if d > e and e - d == d - c:
                            sum = a + b + c + d + e
                            if not min or sum < min:
                                min = sum
                                