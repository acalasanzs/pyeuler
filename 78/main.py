def p(n):
    first = [1 for _ in range(n)]                   #First combination
    results = [first.copy()]                        #Total combinations list
    cantidad_de_vacios = 1                          #Cantidad de vacíos
    while cantidad_de_vacios < n:                   # Mientras la cantidad de vacios sea menor que n, es decir, todos los vacios disponibles

        """ Función que actualiza según los indices los vacios a añadir en first.copy() """
        def update(index):
            actual = first.copy()                       # Hacer una copia de la primera combinación para modificarla
            for current in index:
                actual.insert(current, 0)
            for arr in results:
                try:
                    if all([True if arr[idx] == actual[idx] else False for idx in range(len(actual))]) or all([True if arr[idx] == actual[len(actual)-idx] else False for idx in range(len(actual))]):
                        return False
                    else:
                        continue
                except IndexError:
                    pass
            results.append(actual)
            return True
        index = [i for i in range(1, cantidad_de_vacios*2, 2)]
        update(index)

        for i in range(cantidad_de_vacios):
            existent = False
            while not existent:
                without_it = index.copy()
                last = without_it[i]
                without_it.pop(i)
                index[i] += 2
                while index[i] in without_it:
                    index[i] += 2
                if index[i] > index[-1]:
                    index[i] = last
                    break
                existent = update(index)
        cantidad_de_vacios += 1
    return results

for x in p(5):
    print(x)
