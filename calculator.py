# =============================================================================
# Copyright 2023-2025 Autor da HandTrackify.
#
# Arquivo: calculator.py
# Criado por: Braian E.C. Vidal
# Data de Criação: 10/12/2023
# Última Modificação por: Braian E.C. Vidal
# Data da Última Modificação: 10/12/2023
# Licença: GNU General Public License v3.0
# Link da Licença: https://github.com/Braian555/HandTrackify/blob/main/LICENSE
#
# =============================================================================

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x600")
        self.configure(bg="#f0f0f0")  # Cor de fundo

        self.resultado_var = tk.StringVar()

        # Entrada para exibir o resultado
        entrada = tk.Entry(self, textvariable=self.resultado_var, font=('Helvetica', 20), justify='right', bd=10)
        entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky='nsew')

        # Botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (texto, linha, coluna) in botoes:
            botao = tk.Button(self, text=texto, padx=20, pady=20, font=('Helvetica', 14), bd=5,
                              command=lambda t=texto: self.botao_clicado(t))
            botao.grid(row=linha, column=coluna, sticky='nsew')

        # Configurar pesos para que os botões e a entrada se expandam
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def botao_clicado(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Erro")
        elif valor == "C":
            self.resultado_var.set("")
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
