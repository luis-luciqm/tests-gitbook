#!/usr/bin/env python3
"""
Calcula uma rota ótima para o Problema do Caixeiro Viajante (TSP)
usando o algoritmo de Held-Karp (programação dinâmica com bitmask).

Também pode gerar um relatório em Markdown com o resultado.
"""

from __future__ import annotations

import argparse
import itertools
import math
import random
from pathlib import Path


def build_random_distance_matrix(size: int, seed: int | None = None) -> list[list[float]]:
    rng = random.Random(seed)
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(i + 1, size):
            value = rng.uniform(10, 300)
            matrix[i][j] = value
            matrix[j][i] = value
    return matrix


def held_karp_tsp(distance: list[list[float]]) -> tuple[float, list[int]]:
    n = len(distance)
    if n < 2:
        return 0.0, [0]

    dp: dict[tuple[int, int], tuple[float, int]] = {}

    for k in range(1, n):
        dp[(1 << k, k)] = (distance[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev_bits = bits & ~(1 << k)
                best_cost = math.inf
                best_parent = -1

                for m in subset:
                    if m == k:
                        continue
                    prev_cost = dp[(prev_bits, m)][0]
                    cost = prev_cost + distance[m][k]
                    if cost < best_cost:
                        best_cost = cost
                        best_parent = m

                dp[(bits, k)] = (best_cost, best_parent)

    full_bits = (1 << n) - 2
    best_tour_cost = math.inf
    best_last_city = -1

    for k in range(1, n):
        cost = dp[(full_bits, k)][0] + distance[k][0]
        if cost < best_tour_cost:
            best_tour_cost = cost
            best_last_city = k

    route = [0]
    bits = full_bits
    last_city = best_last_city
    order = [last_city]

    for _ in range(n - 2):
        _, parent = dp[(bits, last_city)]
        order.append(parent)
        bits &= ~(1 << last_city)
        last_city = parent

    order.reverse()
    route.extend(order)
    route.append(0)

    return best_tour_cost, route


def write_markdown_report(
    output_path: Path, size: int, cost: float, route: list[int], matrix: list[list[float]]
) -> None:
    lines = [
        "# Relatório de Cálculo Difícil (TSP)",
        "",
        "## Resultado",
        f"- Quantidade de cidades: **{size}**",
        f"- Custo total da rota ótima: **{cost:.2f}**",
        f"- Rota ótima encontrada: **{' -> '.join(map(str, route))}**",
        "",
        "## Matriz de Distâncias",
        "| Cidade | " + " | ".join(str(i) for i in range(size)) + " |",
        "|---|" + "|".join("---" for _ in range(size)) + "|",
    ]

    for i in range(size):
        row = [f"{matrix[i][j]:.1f}" for j in range(size)]
        lines.append(f"| {i} | " + " | ".join(row) + " |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calcula uma rota ótima do TSP usando Held-Karp."
    )
    parser.add_argument(
        "--cities",
        type=int,
        default=10,
        help="Número de cidades para gerar aleatoriamente (padrão: 10).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Semente para reprodutibilidade (padrão: 42).",
    )
    parser.add_argument(
        "--report",
        type=str,
        default=".docs/resultado-tsp.md",
        help="Arquivo markdown de saída do relatório (padrão: .docs/resultado-tsp.md).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.cities < 2:
        raise SystemExit("O número de cidades deve ser >= 2.")

    matrix = build_random_distance_matrix(args.cities, args.seed)
    cost, route = held_karp_tsp(matrix)
    write_markdown_report(Path(args.report), args.cities, cost, route, matrix)

    print("Cálculo concluído.")
    print(f"Cidades: {args.cities}")
    print(f"Custo ótimo: {cost:.2f}")
    print(f"Rota: {' -> '.join(map(str, route))}")
    print(f"Relatório markdown gerado em: {args.report}")


if __name__ == "__main__":
    main()
