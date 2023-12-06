from datetime import datetime


def main():
    P = []
    for j in range(2, 12): # j > 1, and j can at most be 11
        for k in range(1, 13-j): # allows for all values of 13-j-k to map to n.
            n = 13 - j - k
            if n % j**k == 0 and n % j**(k+1) != 0:
                P.append(j*k*n)

    return sum(P)


start_time = datetime.now()
print(main())
end_time = datetime.now()
print(end_time - start_time)
