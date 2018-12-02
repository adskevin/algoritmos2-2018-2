def inverte(fila):
    quantidade = len(fila) - 1
    new_fila = []
    while quantidade >= 0:
        new_fila.append(fila[quantidade])
        quantidade -= 1
    return new_fila


def main():
    fila = [10, 20, 30, 40, 50, 60, 70, 80]
    print(fila)
    fila = inverte(fila)
    print(fila)


main()
