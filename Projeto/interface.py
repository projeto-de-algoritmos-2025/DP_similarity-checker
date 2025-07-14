import tkinter as tk
from tkinter import messagebox, OptionMenu

from alquimista.dados import RECEITAS, ALFABETO_CULINARIO
from alquimista.analisador import alinhar_sequencias_global, calcular_distancia_levenshtein

class AlquimistaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧪 Alquimista Culinário")
        self.root.geometry("720x620")
        self.root.configure(bg="#1f1f2e")  # fundo escuro

        self.passos_usuario = []

        # ---------- TÍTULO ----------
        tk.Label(
            root,
            text="🔮 Alquimista Culinário",
            font=("Helvetica", 22, "bold"),
            bg="#1f1f2e",
            fg="white"
        ).pack(pady=10)

        # ---------- BARRA DE NAVEGAÇÃO ----------
        self.tabs = tk.Frame(root, bg="#1f1f2e")
        self.tabs.pack(pady=10)

        # Estilo invertido (fundo branco, texto preto)
        style_btn = {
            "bg": "white", "fg": "black",
            "relief": "flat", "activebackground": "#dddddd",
            "activeforeground": "black", "bd": 0, "highlightthickness": 0,
            "width": 20
        }

        self.botao_assistente = tk.Button(
            self.tabs, text="👩‍🍳 Assistente", command=self.modo_assistente, **style_btn
        )
        self.botao_assistente.grid(row=0, column=0, padx=10)

        self.botao_comparador = tk.Button(
            self.tabs, text="⚖️ Comparar", command=self.modo_comparador, **style_btn
        )
        self.botao_comparador.grid(row=0, column=1, padx=10)

        # ---------- ÁREA DE CONTEÚDO ----------
        self.frame_conteudo = tk.Frame(root, bg="#1f1f2e")
        self.frame_conteudo.pack(pady=20, fill="both", expand=True)

        # ---------- ÁREA DE RESULTADO ----------
        self.resultado = tk.Label(
            root,
            text="",
            font=("Helvetica", 13),
            bg="#1f1f2e",
            fg="#c2c2ff",
            wraplength=600,
            justify="left"
        )
        self.resultado.pack(pady=10)

    def limpar_frame(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()
        self.resultado.config(text="")

    def modo_assistente(self):
        self.limpar_frame()

        tk.Label(
            self.frame_conteudo,
            text="📝 Selecione os passos desejados da receita abaixo:",
            font=("Helvetica", 12),
            bg="#1f1f2e",
            fg="white"
        ).pack(pady=10)

        # Listbox fixa e visível ao clicar
        self.listbox = tk.Listbox(
            self.frame_conteudo,
            selectmode=tk.MULTIPLE,
            width=60, height=15,
            font=("Helvetica", 10),
            bg="white", fg="black",
            selectbackground="#5568FE", activestyle="none",
            highlightthickness=0, bd=1
        )
        for passo in ALFABETO_CULINARIO:
            self.listbox.insert(tk.END, passo)
        self.listbox.pack(pady=10)

        # Botão Analisar com estilo invertido também
        tk.Button(
            self.frame_conteudo,
            text="🔍 Analisar Receita",
            command=self.analisar_receita,
            bg="white", fg="black",
            relief="flat", activebackground="#dddddd",
            activeforeground="black", bd=0, highlightthickness=0
        ).pack(pady=10)

    def analisar_receita(self):
        selecao = self.listbox.curselection()
        passos_usuario = [self.listbox.get(i) for i in selecao]

        if not passos_usuario:
            messagebox.showwarning("Aviso", "Selecione ao menos um passo!")
            return

        melhor_nome = None
        maior_score = float('-inf')

        for nome, passos in RECEITAS.items():
            score, _ = alinhar_sequencias_global(passos_usuario, passos)
            if score > maior_score:
                maior_score = score
                melhor_nome = nome

        self.resultado.config(
            text=f"🍽️ Receita mais parecida: *{melhor_nome}*\n🎯 Score de Similaridade: {maior_score}"
        )

    def modo_comparador(self):
        self.limpar_frame()

        tk.Label(
            self.frame_conteudo,
            text="📋 Escolha duas receitas para comparar:",
            font=("Helvetica", 12),
            bg="#1f1f2e", fg="white"
        ).pack(pady=10)

        nomes_receitas = list(RECEITAS.keys())

        self.var1 = tk.StringVar(self.frame_conteudo)
        self.var1.set(nomes_receitas[0])
        menu1 = OptionMenu(self.frame_conteudo, self.var1, *nomes_receitas)
        menu1.config(bg="white", fg="black", width=30, relief="flat", activebackground="#dddddd")
        menu1["menu"].config(bg="white", fg="black")
        menu1.pack(pady=5)

        self.var2 = tk.StringVar(self.frame_conteudo)
        self.var2.set(nomes_receitas[1])
        menu2 = OptionMenu(self.frame_conteudo, self.var2, *nomes_receitas)
        menu2.config(bg="white", fg="black", width=30, relief="flat", activebackground="#dddddd")
        menu2["menu"].config(bg="white", fg="black")
        menu2.pack(pady=5)

        tk.Button(
            self.frame_conteudo,
            text="🧬 Comparar (Levenshtein)",
            command=self.comparar_levenshtein,
            bg="white", fg="black", relief="flat", activebackground="#dddddd",
            bd=0, highlightthickness=0
        ).pack(pady=5)

        tk.Button(
            self.frame_conteudo,
            text="🔗 Comparar (Alinhamento)",
            command=self.comparar_score,
            bg="white", fg="black", relief="flat", activebackground="#dddddd",
            bd=0, highlightthickness=0
        ).pack(pady=5)

    def comparar_levenshtein(self):
        r1 = self.var1.get()
        r2 = self.var2.get()
        if r1 == r2:
            messagebox.showwarning("Aviso", "Selecione receitas diferentes.")
            return
        dist, _ = calcular_distancia_levenshtein(RECEITAS[r1], RECEITAS[r2])
        self.resultado.config(
            text=f"📏 Distância entre '{r1}' e '{r2}': {dist}\n(Quanto menor, mais parecidas)"
        )

    def comparar_score(self):
        r1 = self.var1.get()
        r2 = self.var2.get()
        if r1 == r2:
            messagebox.showwarning("Aviso", "Selecione receitas diferentes.")
            return
        score, _ = alinhar_sequencias_global(RECEITAS[r1], RECEITAS[r2])
        self.resultado.config(
            text=f"🎯 Score de Alinhamento entre '{r1}' e '{r2}': {score}\n(Quanto maior, mais parecidas)"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AlquimistaApp(root)
    root.mainloop()
