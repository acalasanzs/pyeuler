def p(n):
    results = [[1 for _ in range(n)]]
    cantidad_de_vacios = 1
    while cantidad_de_vacios < n -1:
        index = [0 for _ in range(cantidad_de_vacios)]
        for x in range(cantidad_de_vacios):
            actual = [1 for _ in range(n)]
            actual.insert(index[x], 0)
            results.append(actual)
        cantidad_de_vacios += 1
    return results

for x in p(5):
    print(x)
