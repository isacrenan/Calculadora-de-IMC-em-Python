import tkinter as tk

class IMCCalculatorWindow:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")

        self.label_peso = tk.Label(master, text="Peso (kg): ")
        self.label_peso.grid(row=0, column=0)

        self.entry_peso = tk.Entry(master)
        self.entry_peso.grid(row=0, column=1)

        self.label_altura = tk.Label(master, text="Altura (m): ")
        self.label_altura.grid(row=1, column=0)

        self.entry_altura = tk.Entry(master)
        self.entry_altura.grid(row=1, column=1)

        self.button_calcular = tk.Button(master, text="Calcular", command=self.calcular_imc)
        self.button_calcular.grid(row=2, columnspan=2)

        self.label_imc = tk.Label(master, text="")
        self.label_imc.grid(row=3, columnspan=2)

        self.label_classificacao = tk.Label(master, text="")
        self.label_classificacao.grid(row=4, columnspan=2)

    def calcular_imc(self):
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        imc = peso / altura**2
        classificacao = self.classificar_imc(imc)
        self.label_imc.config(text="Seu IMC é: {:.2f}".format(imc))
        self.label_classificacao.config(text="Classificação: {}".format(classificacao))

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc >= 18.5 and imc < 25:
            return "Peso normal"
        elif imc >= 25 and imc < 30:
            return "Sobrepeso"
        elif imc >= 30 and imc < 35:
            return "Obesidade Grau I"
        elif imc >= 35 and imc < 40:
            return "Obesidade Grau II"
        else:
            return "Obesidade Grau III"

root = tk.Tk()
app = IMCCalculatorWindow(root)
root.mainloop()
