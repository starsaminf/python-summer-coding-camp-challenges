cube = lambda x: pow(x, 3)

def fibonacci(n):
    a = 0
    b = 1
    aux = 0
    array = []
    for index in range(n):
        array.append(aux)
        a = b
        b = aux
        aux = a + b
    return array

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))