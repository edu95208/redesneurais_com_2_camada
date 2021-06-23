import random

class entradas():
    def __init__(self, valores, pesos):
        self.valores = int(valores)
        self.pesos = dict(pesos)

def somatorio(entradas, pesos):
    print(f'Peso Selecionado = {pesos}')
    constat = 0
    valor_somatorio = 0
    for e in entradas:
        valor_somatorio += e['valor'] * e['pesos'][pesos]
    return round(valor_somatorio + constat, 2)

def cost(valor_got, valor_ideal):
    return round(((valor_got - valor_ideal) ** 2), 2)

def gerador_pesos (qtd_peso):
    pesos = {}
    for n_peso in range(qtd_peso):
        pesos[f'w{n_peso}'] = round(random.random(), 2)
    return pesos

def gerador_list_entradas(qtd_entradas, qtd_pesos_por_entradas):
    entradas = []
    for n_entradas in range(qtd_entradas):
        vars()[f'e{str(n_entradas)}'] = {
            "name": f'entradas {str(n_entradas)}',
            "valor": round(random.random(), 2),
            "pesos": gerador_pesos(qtd_pesos_por_entradas)
        }
        entradas.append(vars()[f'e{str(n_entradas)}'])
    return entradas

def pesos_random(entradas):
    return f'w{str(random.randint(0, len(entradas["pesos"]) - 1))}'

def pesos_random(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'

def print_list_entradas(entradas):
    for item in entradas:
        print(f'{item["name"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')

def list_entradas_total(entradas):
    for item in entradas:
        print(item)
    print('\n')

def runner():
    qtd_entradas= 10
    qtd_peso = 10
    print('\n=-=-=-=-=-=-=-= Início =-=-=-=-=-=-=-=\n')
    print(f'Número de entradas: {qtd_entradas}\nNúmero de pesos: {qtd_peso}\n')

    entry = gerador_list_entradas( qtd_entradas, qtd_peso)
    exit = gerador_list_entradas( qtd_entradas, qtd_peso)
    print('\n')
    print('Lista geradora 1:\n')
    print_list_entradas(entry)
    print('Lista geradora 2:\n')
    print_list_entradas(exit)
    print('\n')

    somatorio1 = somatorio(entry, pesos_random (qtd_peso))
    somatorio2 = somatorio(entry, pesos_random (qtd_peso))

    costantes1 = cost(somatorio1, 1)
    costantes2 = cost(somatorio2, 1)
    ideal = costantes1 - costantes2

    print(f'Valor da função 1: {somatorio1}')
    print(f'Valor da 1ª função: {costantes1}')
    print(f'Valor função 2: {somatorio2}\n')
    print(f'Valor da 2ª função: {costantes2}')

    print('Valor ideal: 4.75')
    print(f'costantes1 - costantes2 = ideal')
    print(f'{costantes1} - {costantes2} = {ideal}\n')

    if ideal < 4.75:
        print(f'Valor abaixo do ideal: {ideal}')
    elif ideal > 4.75:
        print(f'Valor acima do ideal: {ideal}')
    else:
        print(f'Valor ideal a ser atingido: {ideal}')

        print('\n=-=-=-=-=-=-=-= Fim =-=-=-=-=-=-=-=\n')

if __name__ == '__main__':
    runner()