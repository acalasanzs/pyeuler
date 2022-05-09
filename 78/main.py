def p(n):
    first = [1 for _ in range(n)]
    results = [first.copy()]
    cantidad_de_vacios = 1
    while cantidad_de_vacios < n:
        idx = 1
        actual = first.copy()
        while idx < cantidad_de_vacios*2:
            actual.insert(idx, 0)
            idx += 2
        results.append(actual)
        cantidad_de_vacios += 1
    return results

for x in p(5):
    print(x)
