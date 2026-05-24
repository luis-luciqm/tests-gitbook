# Feature: Listagem de Produtos

## Visão Geral
A nova feature de listagem de produtos permite exibir produtos de forma rápida, organizada e com suporte a filtros e ordenação. O objetivo é melhorar a navegação do usuário e facilitar a descoberta de itens no catálogo.

## Objetivos
- Exibir produtos paginados para melhor performance.
- Permitir filtrar produtos por categoria, faixa de preço e disponibilidade.
- Permitir ordenação por relevância, menor preço, maior preço e mais vendidos.
- Melhorar a experiência de busca e descoberta de produtos.

## Escopo da Entrega
- Tela de listagem com cards de produto.
- Paginação com carregamento incremental.
- Barra de filtros com aplicação em tempo real.
- Ordenação por critérios selecionáveis.
- Estado de carregamento, vazio e erro.

## Regras de Negócio
- Apenas produtos ativos devem aparecer na listagem.
- Produtos sem estoque devem ser exibidos como "Indisponível".
- Filtros podem ser combinados entre si.
- A ordenação deve respeitar o conjunto filtrado.
- Ao limpar filtros, a listagem deve voltar ao estado padrão.

## Comportamento da Interface
- Cada card deve apresentar: imagem, nome, preço, desconto (quando houver) e status de estoque.
- A troca de filtros deve atualizar os resultados sem recarregar a página.
- Ao carregar mais itens, manter a posição de rolagem do usuário.
- Exibir mensagem amigável quando nenhum produto for encontrado.

## Critérios de Aceite
- Usuário consegue visualizar a primeira página de produtos ao abrir a tela.
- Usuário consegue aplicar e remover filtros sem inconsistências.
- Usuário consegue alterar ordenação e ver a lista atualizada corretamente.
- Usuário recebe feedback visual durante carregamento.
- Em caso de erro na API, exibir mensagem e opção de tentar novamente.

## Métricas de Sucesso
- Aumento da taxa de clique em produtos na listagem.
- Redução da taxa de abandono na navegação do catálogo.
- Melhoria no tempo médio para encontrar um produto.
- Redução no tempo de carregamento percebido.

## Observações Técnicas
- Endpoint sugerido: `GET /products`
- Parâmetros comuns: `page`, `limit`, `category`, `minPrice`, `maxPrice`, `sort`, `inStock`
- Recomenda-se cache de resultados por combinação de filtros.
- Implementar debounce no campo de busca para reduzir chamadas.
