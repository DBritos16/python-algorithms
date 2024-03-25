history = []

def weird_algorithm(x):
    history.append(x)
    
    while history[len(history)-1] != 1:
        n = history[len(history)-1]

        if n % 2 == 0:
            history.append(n/2)
        else:
            history.append((n*3)+1)
    else:
        return history
        pass

   
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
