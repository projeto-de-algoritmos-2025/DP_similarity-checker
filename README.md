# Alquimista Culinário

**Número da Lista**: 5 <br>
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01   <br>
**Grupo**: 12

## Alunos


<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/BiancaPatrocinio7"><img style="border-radius: 50%;" src="https://github.com/BiancaPatrocinio7.png" width="190;" alt=""/><br /><sub><b>Bianca Patrocínio</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/leticiatmartins"><img style="border-radius: 50%;" src="https://github.com/leticiatmartins.png" width="190px;" alt=""/><br /><sub><b>Leticia Torres </b></sub></a><br />
  </tr>
</table>

| Matrícula   | Aluno                             |
| ----------- | ---------------------------------- |
| 22/1008801  | Bianca Patrocínio Castro           |
| 20/2016702  | Leticia Torres Soares Martins      |
</div>

## Sobre 
O projeto **Alquimista Culinário** é uma aplicação interativa de terminal que utiliza algoritmos de Programação Dinâmica para analisar e comparar receitas de cozinha. A ideia central é tratar cada receita não como uma lista de ingredientes, mas como uma **sequência de ações**, permitindo uma análise de similaridade de processos.

O sistema implementa dois algoritmos clássicos de alinhamento de sequências para realizar suas análises:
1.  **Distância de Levenshtein**: Calcula o **custo mínimo** (número de edições: inserção, exclusão, substituição) para transformar uma receita em outra. Um valor baixo indica alta similaridade.
2.  **Alinhamento Global de Sequências (Needleman-Wunsch)**: Calcula um **score máximo** de alinhamento entre duas receitas, recompensando passos em comum e penalizando diferenças e lacunas. Um valor alto indica alta similaridade.

O programa oferece duas funcionalidades principais:
- **Assistente Culinário**: O usuário seleciona uma sequência de passos de uma lista, e o sistema utiliza o algoritmo de alinhamento por score para determinar qual das receitas em seu banco de dados é a mais parecida com o que o usuário deseja fazer.
- **Comparador de Receitas**: Permite ao usuário escolher duas receitas existentes e compará-las usando tanto a métrica de Distância de Levenshtein quanto o Score de Alinhamento, oferecendo duas visões complementares da similaridade.

## Screenshots
1.  Screenshot do Menu Principal.
2.  Screenshot do "Modo Assistente Culinário" mostrando a lista de passos e a seleção do usuário.
3.  Screenshot do resultado da análise do assistente.
4.  Screenshot do resultado de uma comparação por Distância e por Score.

## Instalação 
**Linguagem**: Python

## Pré-requisitos

Antes de rodar o projeto, você precisará ter o **Python 3** instalado em seu sistema. Nenhuma biblioteca externa é necessária.

### Instalar Python

#### No Windows:
Baixe o instalador diretamente do [site oficial do Python](https://www.python.org/downloads/) e siga as instruções. **Lembre-se de marcar a opção "Add Python to PATH"** durante a instalação.

#### No macOS:
O Python 3 geralmente já vem instalado. Você pode verificar com o comando `python3 --version`. Caso precise instalar, use o [Homebrew](https://brew.sh/):
```bash
brew install python
```

## 🚀 Como compilar e executar o projeto

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/projeto-de-algoritmos-2025/DC_Analisador_de_Afinidade_Musical.git
cd DC_Analisador_de_Afinidade_Musical
```

---

### Passo 2: (Opcional) Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

---

### Passo 3: Entrar na pasta projeto

```bash
cd Projeto/
```

---

### Passo 4: Rodar o projeto 
- Visualizar pelo terminal

```bash
python main.py
```
ou

```bash
python3 main.py
```

- Visualizar pela interface
```bash
python gui.py
```
ou

```bash
python3 gui.py
```

---
## 📽️ Apresentação

<div align="center">
<a href="https://youtu.be/tx-iWso1guE?si=0JcJjfdS03mmx4G2"><img src="Documentos/screenshots/image4.png" width="50%"></a>
</div>


<font size="3"><p style="text-align: center">Autoras: [Bianca Patrocínio](https://github.com/BiancaPatrocinio7) e [Letícia Torres](https://github.com/leticiatmartins).</p></font>


---
