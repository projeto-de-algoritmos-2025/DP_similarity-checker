"""
Módulo Analisador.

Contém implementações de algoritmos de programação dinâmica para
comparar sequências de receitas.
"""

def calcular_distancia_levenshtein(receita1: list, receita2: list) -> tuple[int, list[list[int]]]:
    len1, len2 = len(receita1), len(receita2)
    matriz = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    for i in range(len1 + 1):
        matriz[i][0] = i
    for j in range(len2 + 1):
        matriz[0][j] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            custo = 0 if receita1[i-1] == receita2[j-1] else 1
            custo_delecao = matriz[i-1][j] + 1
            custo_insercao = matriz[i][j-1] + 1
            custo_substituicao = matriz[i-1][j-1] + custo
            matriz[i][j] = min(custo_delecao, custo_insercao, custo_substituicao)
    distancia = matriz[len1][len2]
    return distancia, matriz



def alinhar_sequencias_global(receita1: list, receita2: list) -> tuple[int, list[list[int]]]:
    """
    Calcula o score de alinhamento global entre duas receitas (Needleman-Wunsch).

    Um score ALTO indica alta similaridade.

    Args:
        receita1: A primeira sequência de ações.
        receita2: A segunda sequência de ações.

    Returns:
        Uma tupla contendo o score final (int) e a matriz de
        programação dinâmica completa (list[list[int]]).
    """
    MATCH_SCORE = 2         
    MISMATCH_PENALTY = -1   
    GAP_PENALTY = -2       

    len1, len2 = len(receita1), len(receita2)
    matriz = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        matriz[i][0] = i * GAP_PENALTY
    for j in range(1, len2 + 1):
        matriz[0][j] = j * GAP_PENALTY

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if receita1[i-1] == receita2[j-1]:
                score_alinhamento = matriz[i-1][j-1] + MATCH_SCORE
            else:
                score_alinhamento = matriz[i-1][j-1] + MISMATCH_PENALTY
            
            score_delecao = matriz[i-1][j] + GAP_PENALTY

            score_insercao = matriz[i][j-1] + GAP_PENALTY

            matriz[i][j] = max(score_alinhamento, score_delecao, score_insercao)

    score = matriz[len1][len2]

    return score, matriz