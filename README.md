# Algoritmo A*

Este é um algoritmo de busca de caminho (A Star) que encontra a rota mais curta entre dois pontos em um mapa considerando o custo associado a cada local no mapa.

## Como utilizar

- O código implementa o algoritmo para calcular o menor caminho em dois mapas pré-definidos nos arquivos mapa-1.txt e mapa2.txt.
- Ao executar o arquivo a-star.py, o terminal solicitará que você informe as coordenadas X e Y do destino desejado.
- Após a entrada das coordenadas, o sistema calculará e mostrará o menor caminho percorrido no mapa-1, que tem o seguinte formato:

### Mapa 1:
> Origem:
> 
> 0 7
> 
> Mapa:
> 
> 0  0  0  0  0  0  0  0  0  0
> 
> 0  0  0  0  0  0  0  0  0  0
> 
> 0  0  0 -1 -1 -1 -1 -1  0  0
> 
> 0  0  0  0  0  0  0 -1  0  0
> 
> 0  0  0  0  0  0  0 -1  0  0
> 
> 0  0  0  0  0  0  0 -1  0  0
> 
> 0  0  0  0  0  0  0  0  0  0
> 
> 0  0  0  0  0  0  0  0  0  0

- Em seguida, o sistema solicitará novamente no terminal as coordenadas X e Y do destino para o segundo mapa:

### Mapa 2:
> Origem:
> 
> 0 7
> 
> Mapa:
> 
> 3  1  4 -1 -1  8  8  8  0  0
> 
> 3  3  2  6  2  3  8  8  1  0
> 
> 3  3  3  5  6  8 10  6  1  0
> 
> 0  1  1  4  0 10 10 -1  1  0
> 
> 0  1  1  4  5  0  0 -1  1  0
> 
> 0  1  1  1  1  0  0 -1  1  0
> 
> 0  1  1  1  1  1 10 10  3  0
> 
> 0  0  0  0  0  0 10 10 10  0
