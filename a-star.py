import heapq

# Movimentos possíveis
movimentos = [
                (0,  1), #↓
                (0, -1), #↑
                (1,  0), #→
                (-1, 0)  #←
            ]

# Ler o arquivo
def ler_mapa(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        largura, altura = map(int, linhas[0].split())
        origem = tuple(map(int, linhas[1].split()))

        mapa = []
        for linha in linhas[2:]:
            linha = list(map(int, linha.split()))
            mapa.append(linha)

    return largura, altura, origem, mapa

# Algorítmo A*
def a_star(largura, altura, origem, destino, mapa):
    # Verificar se tem o destino
    if destino[0] < 0 or destino[0] >= largura or destino[1] < 0 or destino[1] >= altura:
        return "Destino está fora do mapa."

    abertos = [(0, origem)]
    heapq.heapify(abertos)
    custo_atual = {origem: 0}
    caminho_anterior = {}

    # Loop principal do algoritmo A*
    while abertos:
        _, atual = heapq.heappop(abertos)

        if atual == destino:
            # Se chegar ao destino, recaptula caminho
            caminho = []
            while atual in caminho_anterior:
                caminho.insert(0, atual)
                atual = caminho_anterior[atual]
            caminho.insert(0, origem)
            return caminho

        for dx, dy in movimentos:
            novo_x, novo_y = atual[0] + dx, atual[1] + dy

            if 0 <= novo_x < largura and 0 <= novo_y < altura and mapa[novo_y][novo_x] != -1:
                custo = custo_atual[atual] + mapa[novo_y][novo_x]
                if (novo_x, novo_y) not in custo_atual or custo < custo_atual[(novo_x, novo_y)]:
                    custo_atual[(novo_x, novo_y)] = custo
                    prioridade = custo + heuristica(destino, (novo_x, novo_y))
                    heapq.heappush(abertos, (prioridade, (novo_x, novo_y)))
                    caminho_anterior[(novo_x, novo_y)] = atual

    return "Não foi possível encontrar um caminho."

# Função heurística para o custo
def heuristica(destino, ponto):
    return abs(destino[0] - ponto[0]) + abs(destino[1] - ponto[1])

# Função para imprimir o mapa e o caminho percorrido
def imprimir_caminho(mapa, caminho):
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if (x, y) in caminho:
                print(' #', end=' ')
            else:
                print(f"{mapa[y][x]:>2}", end=' ')
        print()

# Função principal
def main():
    arquivo_mapa = 'mapa-1.txt'  # Nome do arquivo com o mapa
    x = int(input("Informe o x do destino: "))
    y = int(input("Informe o y do destino: "))
    destino = (x, y)  # Coordenada de destino

    largura, altura, origem, mapa = ler_mapa(arquivo_mapa)

    resultado = a_star(largura, altura, origem, destino, mapa)

    if isinstance(resultado, list):
        print(f"Caminho percorrido:")
        imprimir_caminho(mapa, resultado)
        print(f"Custo total do caminho: {sum(mapa[y][x] for x, y in resultado)}")
        print(f"Coordenadas percorridas: {resultado}")
    else:
        print(resultado)

    arquivo_mapa = 'mapa-2.txt'  # Nome do arquivo com o mapa
    x = int(input("Informe o x do destino: "))
    y = int(input("Informe o y do destino: "))
    destino = (x, y)  # Coordenada de destino

    largura, altura, origem, mapa = ler_mapa(arquivo_mapa)

    resultado = a_star(largura, altura, origem, destino, mapa)

    if isinstance(resultado, list):
        print(f"Caminho percorrido:")
        imprimir_caminho(mapa, resultado)
        print(f"Custo total do caminho: {sum(mapa[y][x] for x, y in resultado)}")
        print(f"Coordenadas percorridas: {resultado}")
    else:
        print(resultado)

main()