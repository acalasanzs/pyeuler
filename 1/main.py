def multiples_de_3_o_5(maximo):
    actual = maximo -1
    cantidad_total = 3
    while actual > 3:
        if actual % 3 == 0 or actual % 5 == 0:
            cantidad_total += actual
        actual -= 1
    return cantidad_total

print(multiples_de_3_o_5(1000))