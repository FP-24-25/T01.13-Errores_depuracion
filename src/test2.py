## Error en tiempo de ejecución: Error de nombre
import random
def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios= []
    for _ in range(num):
        aleatorios.append(random.randint(limite_inf,limite_sup))
    return aleatorios   

if __name__== "__main__":
    print(generar_aleatorios(2, 100, 5))