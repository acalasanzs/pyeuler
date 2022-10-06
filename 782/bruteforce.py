def C(N):
    total = 0
    for x in range(0, N**2):
        total += (N**2) ** x
        print(x)
    return total
print(C(10**4))