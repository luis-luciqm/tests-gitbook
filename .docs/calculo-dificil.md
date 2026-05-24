# Cálculo Difícil: Rota Ótima no Problema do Caixeiro Viajante (TSP)

## O que este cálculo resolve
Este projeto implementa um cálculo considerado difícil em otimização combinatória: encontrar a **rota de menor custo** que passa por todas as cidades exatamente uma vez e retorna ao ponto inicial.

Esse problema é conhecido como **Travelling Salesman Problem (TSP)** e é clássico por sua complexidade computacional.

## Por que é difícil
- O número de rotas possíveis cresce de forma fatorial.
- Para `n` cidades, há aproximadamente `(n-1)!/2` rotas distintas no caso simétrico.
- Testar todas as combinações rapidamente se torna inviável.

## Algoritmo utilizado
Foi implementado o algoritmo **Held-Karp** (Programação Dinâmica com bitmask), que:
- reduz drasticamente o custo em relação à força bruta;
- utiliza subproblemas para compor a solução ótima global;
- garante resultado ótimo (não é heurística).

### Complexidade
- Tempo: `O(n^2 * 2^n)`
- Memória: `O(n * 2^n)`

Apesar de ainda ser exponencial, é muito melhor do que a busca completa.

## Arquivo criado
- Script principal: `setup.py`
- Função central: `held_karp_tsp(distance)`

## Como executar
No diretório do projeto:

```bash
python3 setup.py
```

### Opções úteis
```bash
python3 setup.py --cities 12 --seed 123 --report .docs/resultado-tsp.md
```

- `--cities`: quantidade de cidades geradas aleatoriamente.
- `--seed`: garante reprodutibilidade dos dados.
- `--report`: caminho do arquivo `.md` que será gerado com os resultados.

## Saída gerada
Ao rodar o script, ele:
- calcula a rota ótima;
- imprime custo e caminho no terminal;
- gera um relatório Markdown com:
  - custo total ótimo;
  - sequência da rota;
  - matriz de distâncias em tabela.

Por padrão, o relatório é salvo em:

`/.docs/resultado-tsp.md`

## Exemplo de uso prático
Esse tipo de cálculo é útil para:
- roteirização logística;
- otimização de coletas e entregas;
- planejamento de trajetos de inspeção;
- redução de custos operacionais em deslocamento.
