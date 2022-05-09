def p(n):
    first = [1 for _ in range(n)]                   # Primera combinación
    results = [first.copy()]                        # Lista total de combinaciones
    cantidad_de_vacios = 1                          # Cantidad de vacíos
    while cantidad_de_vacios < n:                   # Mientras la cantidad de vacios sea menor que n, es decir, todos los vacios disponibles

        """ Función que actualiza según los indices los vacios a añadir en first.copy() """
        def update(index):
            actual = first.copy()                       # Hacer una copia de la primera combinación para modificarla
            for current in index:                       # Por cada indíce de los índices adonde poner vacios insertar un 0 en dicha posición
                actual.insert(current, 0)
            for arr in results:                         # Comprovar si ya existe en results actual
                try:
                    if all([True if arr[idx] == actual[idx] else False for idx in range(len(actual))]) or all([True if arr[idx] == actual[len(actual)-idx] else False for idx in range(len(actual))]):
                        return False                    # Devolver falso en caso de que se encuentre una repetición
                    else:
                        continue
                except IndexError:
                    pass
            results.append(actual)                      # Añadir a results actual
            return True                                 # En caso de éxito devolver True

        """ Interponer todos los índices en saltos de 2 desde la posición 1 y actualizar """
        index = [i for i in range(1, cantidad_de_vacios*2, 2)] 
        update(index)

        """ Por cada vacio que se debe interponer """
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
