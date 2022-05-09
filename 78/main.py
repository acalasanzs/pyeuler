import numpy as np
def p(n):
    first = [1 for _ in range(n)]
    results = [first.copy()]
    cantidad_de_vacios = 1
    while cantidad_de_vacios < n:
        actual = first.copy()
        existent = False
        def update(index):
            for current in index:
                actual.insert(current, 0)
            for arr in results:
                if np.array_equal(arr, actual):
                    existent = True
                    return
            results.append(actual)
        index = [i for i in range(1, cantidad_de_vacios*2, 2)]
        #update(index)
        for i in range(cantidad_de_vacios):
            while not existent:
                without_it = index.copy()
                last = without_it[i]
                without_it.pop(i)
                index[i] += 2
                while index[i] in without_it:
                    index[i] += 2
                if index[i] > index[-1]:
                    index[i] = last
                    continue
                update(index)
            existent = False
        cantidad_de_vacios += 1
    return results

for x in p(5):
    print(x)
