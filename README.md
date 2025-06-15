
# Projeto Flood Fill - Colorindo Regiões (Versão para Terminal)

## Descrição do Projeto
Este projeto implementa o algoritmo Flood Fill em Python para uso em terminal, conforme especificado no "Trabalho em grupo 2" da disciplina Fundamentos de Projeto e Análise de Algoritmos da PUC Minas. O sistema simula um robô mapeando um terreno, onde uma grade 2D representa áreas navegáveis (0), obstáculos (1) e regiões coloridas (2, 3, 4, etc.). O algoritmo colore regiões navegáveis conectadas a partir de uma célula especificada pelo usuário, respeitando obstáculos e regiões já coloridas, e continua até que todas as células navegáveis sejam coloridas. A grade é exibida como uma matriz de números no terminal.

## Introdução ao Problema
O problema envolve uma grade 2D onde cada célula é navegável (0), um obstáculo (1) ou uma região previamente colorida (2, 3, 4, ...). O algoritmo Flood Fill é usado para:
- Iniciar a partir de uma célula especificada pelo usuário (x, y).
- Colorir todas as células navegáveis conectadas (0) com uma cor específica (por exemplo, 2 para a primeira região, 3 para a próxima, etc.).
- Respeitar obstáculos (1) e regiões já coloridas (>1).
- Encontrar e colorir automaticamente a próxima região navegável até que todas as células navegáveis sejam coloridas.

A solução é um programa Python baseado em terminal que solicita dimensões da grade, gera e exibe uma grade aleatória, solicita as coordenadas iniciais e exibe a grade antes e depois da aplicação do algoritmo Flood Fill.

## Instruções de Configuração e Execução
1. **Pré-requisitos**: Python 3.6 ou superior instalado.
2. **Configuração**:
   - Baixe o arquivo `main.py` do repositório.
   - Nenhuma biblioteca adicional é necessária, pois o script usa apenas o módulo padrão `random`.
3. **Executando o Projeto**:
   - Abra um terminal e navegue até o diretório que contém `mainl.py`.
   - Execute o script com: `python main.py`.
   - Siga as instruções para inserir:
     - Número de linhas (1-50).
     - Número de colunas (1-50).
   - O programa gerará e exibirá uma grade aleatória com 30% de chance de obstáculos por célula.
   - Em seguida, insira a linha e a coluna inicial (devem estar dentro dos limites e ser navegáveis, ou seja, valor 0).
   - O programa irá:
     - Aplicar o algoritmo Flood Fill começando pela célula especificada, depois preencher automaticamente as regiões navegáveis restantes.
     - Exibir a grade final com regiões coloridas (representadas por números 2, 3, 4, ...).
4. **Repositório**: Certifique-se de que o repositório esteja público ou acessível. Teste o acesso em uma aba anônima do navegador antes da entrega.

## Explicação do Algoritmo Flood Fill
O algoritmo Flood Fill é implementado recursivamente para colorir regiões conectadas:
- **Entrada**: Uma grade 2D (n × m), coordenadas iniciais (x, y) e um valor de cor.
- **Processo**:
  1. Verifica se a célula atual (x, y) está dentro dos limites e é navegável (valor 0).
  2. Se válida, define o valor da célula como a cor atual.
  3. Aplica recursivamente o algoritmo às quatro células adjacentes ortogonalmente (cima, baixo, esquerda, direita).
  4. Ignora células fora dos limites, obstáculos (1) ou já coloridas (>1).
- **Automação**: Após colorir a região inicial especificada pelo usuário, o programa varre a grade em busca da próxima célula navegável (0) e aplica o Flood Fill com a próxima cor (incrementando a partir de 2).
- **Término**: O processo para quando não há mais células navegáveis.
- **Visualização**: A grade é exibida no terminal como uma matriz de números, com 0 para células navegáveis, 1 para obstáculos e 2, 3, 4, ... para regiões coloridas (representando 21 cores distintas, por exemplo, 2 para Vermelho, 3 para Laranja, etc.).
- **Eficiência**: A implementação recursiva é direta e eficaz para grades pequenas a médias. Para grades muito grandes, uma abordagem iterativa (por exemplo, usando uma pilha ou fila) poderia melhorar o desempenho, mas esta solução prioriza clareza e correção.

## Exemplos de Entrada e Saída
### Exemplo 1
**Entrada**:
```
Digite o número de linhas (1-50): 4
Digite o número de colunas (1-50): 5
Grade Inicial:
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
Digite a linha inicial (0-3): 0
Digite a coluna inicial (0-4): 0
```
**Saída**:
```
Grade Final:
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 2
**Entrada**:
```
Digite o número de linhas (1-50): 4
Digite o número de colunas (1-50): 5
Grade Inicial:
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
Digite a linha inicial (0-3): 0
Digite a coluna inicial (0-4): 2
```
**Saída**:
```
Grade Final:
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```


## Recursos Adicionais
- **Tamanho da Grade Configurável**: Os usuários podem especificar o número de linhas e colunas (1 a 50) via entrada no terminal.
- **Célula Inicial Especificada pelo Usuário**: Os usuários podem selecionar a célula inicial (linha, coluna) para o primeiro Flood Fill, que deve ser uma célula navegável (valor 0) dentro dos limites da grade, após visualizar a grade inicial.
- **Cores de Região Predefinidas**: 21 cores distintas são representadas por números (2 a 22), correspondendo a cores como Vermelho, Laranja, Amarelo, Verde, Azul, etc., para consistência com a versão gráfica.
- **Geração Aleatória de Grade**: O programa gera uma grade com 30% de chance de obstáculos por célula.
- **Saída no Terminal**: A grade é exibida como uma matriz de números antes de solicitar a célula inicial e após o Flood Fill, atendendo ao requisito de visualização no terminal.

## Organização do Código
- O código está contido em um único arquivo `main.py` para simplicidade.
- Funções principais:
  - `create_grid`: Gera uma grade aleatória.
  - `print_grid`: Exibe a grade como uma matriz.
  - `main`: Implementa o algoritmo Flood Fill recursivo.
  - `main`: Gerencia a entrada do usuário, validação, exibição da grade e fluxo do programa.

