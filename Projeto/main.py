from alquimista.dados import RECEITAS, ALFABETO_CULINARIO
from alquimista.analisador import calcular_distancia_levenshtein, alinhar_sequencias_global
import time

def exibir_alfabeto_numerado():
    """Mostra ao usuário os passos de receita numerados."""
    print("\n--- PASSOS DE RECEITA DISPONÍVEIS ---")
    for i, passo in enumerate(ALFABETO_CULINARIO, 1):
        print(f"  [{i:02d}] - {passo}")
    print("  [ 0] - CONCLUIR (Analisar meus passos)")
    print("----------------------------------------")

def modo_assistente_culinario():
    """
    Função para o modo 'Descobrir Receita', usando ALINHAMENTO POR SCORE
    para encontrar a receita com a maior pontuação de similaridade.
    """
    print("\n--- MODO ASSISTENTE CULINÁRIO ---")
    print("Selecione os números dos passos que você quer fazer, um por um.")
    
    passos_do_usuario = []
    while True:
        exibir_alfabeto_numerado()
        
        if passos_do_usuario:
            print(f"Seus passos até agora: {', '.join(passos_do_usuario)}")

        try:
            escolha_num = int(input("Digite o NÚMERO do passo que deseja adicionar (ou 0 para concluir): "))
            
            if escolha_num == 0:
                if not passos_do_usuario:
                    print("\nVocê não selecionou nenhum passo. Voltando ao menu.")
                    return
                break 
            
            if 1 <= escolha_num <= len(ALFABETO_CULINARIO):
                passo_selecionado = ALFABETO_CULINARIO[escolha_num - 1]
                passos_do_usuario.append(passo_selecionado)
                print(f"\n[OK] Passo '{passo_selecionado}' adicionado com sucesso!")
                time.sleep(0.7) 
            else:
                print(f"\n[ERRO] Número inválido. Por favor, escolha um número da lista.")
                time.sleep(1)

        except ValueError:
            print("\n[ERRO] Entrada inválida. Por favor, digite apenas o número.")
            time.sleep(1)

    print("\nAnalisando seus passos e comparando com meu livro de receitas...")
    time.sleep(1.5)

    melhor_receita_nome = None
    maior_score = float('-inf') 

    for nome, sequencia in RECEITAS.items():
        score, _ = alinhar_sequencias_global(passos_do_usuario, sequencia)
        
        if score > maior_score:
            maior_score = score
            melhor_receita_nome = nome
    
    print("\n" + "-" * 30)
    print("      RESULTADO DA ANÁLISE")
    print("-" * 30)
    print(f"Com base nos seus passos, a receita com o MAIOR SCORE de similaridade é:")
    print(f"-> Receita Sugerida: {melhor_receita_nome}")
    print(f"\nO 'score de alinhamento' entre seus passos e esta receita foi de {maior_score}.")
    print("Quanto maior o score, mais passos em comum vocês têm!")


def modo_comparador(usar_alinhamento_score=False):
    """
    Função para o modo 'Comparar Duas Receitas'.
    Pode usar Distância de Levenshtein ou Alinhamento por Score.
    """
    if usar_alinhamento_score:
        print("\n--- MODO COMPARADOR (POR SCORE DE ALINHAMENTO) ---")
    else:
        print("\n--- MODO COMPARADOR (POR DISTÂNCIA) ---")

    nomes_receitas = list(RECEITAS.keys())
    
    for i, nome in enumerate(nomes_receitas, 1):
        print(f"  [{i}] - {nome}")
    print("  [0] - Voltar ao menu principal")
    print("-" * 40)
    
    try:
        print("Escolha a PRIMEIRA receita para comparar.")
        escolha1 = int(input("Digite o NÚMERO da receita: "))
        if escolha1 == 0: return

        print("\nEscolha a SEGUNDA receita para comparar.")
        escolha2 = int(input("Digite o NÚMERO da receita: "))
        if escolha2 == 0: return

        if not (0 < escolha1 <= len(nomes_receitas) and 0 < escolha2 <= len(nomes_receitas)):
            print("\n[ERRO] Escolha inválida. Voltando ao menu.")
            return

        receita_a_nome = nomes_receitas[escolha1 - 1]
        receita_b_nome = nomes_receitas[escolha2 - 1]
        receita_a = RECEITAS[receita_a_nome]
        receita_b = RECEITAS[receita_b_nome]

        print("\n" + "-" * 30)
        
        if usar_alinhamento_score:
            score, _ = alinhar_sequencias_global(receita_a, receita_b)
            print(f"O SCORE de alinhamento entre '{receita_a_nome}' e '{receita_b_nome}' é: {score}")
            print("(Quanto MAIOR o score, MAIS SIMILARES são as receitas)")
        else:
            distancia, _ = calcular_distancia_levenshtein(receita_a, receita_b)
            print(f"A DISTÂNCIA entre '{receita_a_nome}' e '{receita_b_nome}' é: {distancia}")
            print("(Quanto MENOR a distância, MAIS SIMILARES são as receitas)")

        print("-" * 30)

    except ValueError:
        print("\n[ERRO] Entrada inválida. Voltando ao menu.")


def main():
    """Função principal que executa o menu principal."""
    print("\nBem-vindo ao Alquimista Culinário!")
    
    while True:
        print("\n" + "="*40)
        print("            MENU PRINCIPAL")
        print("="*40)
        print("  [1] - Descobrir receita (O que posso fazer?)")
        print("  [2] - Comparar por Distância (Levenshtein)")
        print("  [3] - Comparar por Score (Alinhamento)")
        print("  [4] - Sair do programa")
        print("-" * 40)
        
        escolha = input("O que você gostaria de fazer? Digite o número: ")

        if escolha == '1':
            modo_assistente_culinario()
        elif escolha == '2':
            modo_comparador(usar_alinhamento_score=False)
        elif escolha == '3':
            modo_comparador(usar_alinhamento_score=True)
        elif escolha == '4':
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, escolha uma das opções acima.")
        
        input("\nPressione Enter para voltar ao menu principal...")

    print("\nObrigado por usar o Alquimista Culinário. Até a próxima!")


if __name__ == "__main__":
    main()