actual = 2
numerador = 4
denominador = 1
while not(actual == 50000):
    denominador *= 2 - (actual+1)/actual
    actual += 1
print(numerador/denominador)