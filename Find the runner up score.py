if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list()
    for e in arr:
        lista.append(e)
    maior, runner = -101, -101  #Limite inferior
    for e in lista:
        if (e>maior):
            runner = maior
            maior = e
        if (e>runner and e<maior):
            runner = e
    print(runner)
