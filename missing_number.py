def missing_number(length, list):
    x = list[0]
    for i in range(0, length):
        if list[i] != x:
            return x
        else:
            x+=1


assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"