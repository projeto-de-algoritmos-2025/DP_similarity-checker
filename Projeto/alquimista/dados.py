"""
Módulo de Dados para o Alquimista Culinário.

Define o "alfabeto" de ações possíveis na cozinha e armazena as
receitas como sequências dessas ações.
"""

ALFABETO_CULINARIO = [
    "quebrar_ovos", "bater_ovos", "adicionar_ovos", "adicionar_sal", 
    "misturar_secos", "bater_massa", "adicionar_leite", "adicionar_oleo",
    "adicionar_agua", "adicionar_acucar", "adicionar_tempero", "temperar",

    "aquecer_frigideira", "despejar_massa", "fritar", "grelhar", "refogar",
    "ferver", "cozinhar", "assar_180c", "escorrer",

    "descascar_fruta", "cortar_fruta", "picar_legumes", "lavar_ingredientes",
    "marinar", "espremer_fruta",

    "dobrar", "esfriar", "servir", "montar_prato", "adicionar_gelo", 
    "liquidificar", "levar_a_geladeira"
]

RECEITAS = {
    "Omelete Simples": [
        "quebrar_ovos",
        "bater_ovos",
        "adicionar_sal",
        "aquecer_frigideira",
        "despejar_massa",
        "fritar",
        "dobrar",
        "servir"
    ],
    "Bolo de Chocolate": [
        "misturar_secos",
        "adicionar_ovos",
        "adicionar_leite",
        "adicionar_oleo",
        "bater_massa",
        "despejar_massa",
        "assar_180c",
        "esfriar",
        "servir"
    ],
    "Vitamina de Banana": [
        "descascar_fruta",
        "cortar_fruta",
        "adicionar_leite",
        "adicionar_gelo",
        "liquidificar",
        "servir"
    ],
    
    "Arroz Branco Simples": [
        "lavar_ingredientes",
        "refogar",
        "adicionar_agua",
        "adicionar_sal",
        "ferver",
        "cozinhar",
        "servir"
    ],
    "Macarrao Alho e Oleo": [
        "ferver",
        "adicionar_agua",
        "adicionar_sal",
        "cozinhar",
        "escorrer",
        "aquecer_frigideira",
        "adicionar_oleo",
        "refogar",
        "servir"
    ],
    "Frango Grelhado": [
        "temperar",
        "marinar",
        "aquecer_frigideira",
        "grelhar",
        "servir"
    ],
    "Pure de Batata": [
        "lavar_ingredientes",
        "picar_legumes",
        "cozinhar",
        "escorrer",
        "bater_massa", 
        "adicionar_leite",
        "servir"
    ],
    "Bife Acebolado": [
        "temperar",
        "aquecer_frigideira",
        "adicionar_oleo",
        "fritar",
        "picar_legumes",
        "refogar",
        "servir"
    ],
    "Brigadeiro de Panela": [
        "misturar_secos",
        "adicionar_leite",
        "cozinhar",
        "esfriar",
        "servir"
    ],
    "Suco de Laranja Natural": [
        "lavar_ingredientes",
        "cortar_fruta",
        "espremer_fruta",
        "adicionar_gelo",
        "servir"
    ],
    "Limonada Suica": [
        "lavar_ingredientes",
        "cortar_fruta",
        "liquidificar",
        "adicionar_agua",
        "adicionar_acucar",
        "adicionar_gelo",
        "servir"
    ],
    "Panqueca Americana": [
        "misturar_secos",
        "adicionar_ovos",
        "adicionar_leite",
        "bater_massa",
        "aquecer_frigideira",
        "despejar_massa",
        "fritar",
        "servir"
    ],
    "Mousse de Maracuja": [
        "liquidificar",
        "adicionar_leite",
        "levar_a_geladeira",
        "servir"
    ],
    "Pudim de Leite Condensado": [
        "bater_ovos",
        "adicionar_leite",
        "liquidificar",
        "despejar_massa",
        "assar_180c",
        "esfriar",
        "levar_a_geladeira",
        "servir"
    ],
    "Sopa de Legumes": [
        "lavar_ingredientes",
        "picar_legumes",
        "refogar",
        "adicionar_agua",
        "cozinhar",
        "temperar",
        "servir"
    ],
    "Ovo Cozido": [
        "adicionar_agua",
        "ferver",
        "cozinhar",
        "esfriar",
        "descascar_fruta",
        "servir"
    ],
    "Cafe Coado": [
        "ferver",
        "adicionar_agua",
        "escorrer", 
        "servir"
    ],
    "Salada Simples": [
        "lavar_ingredientes",
        "picar_legumes",
        "temperar",
        "montar_prato",
        "servir"
    ]
}