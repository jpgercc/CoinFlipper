import random
import tkinter as tk


def exibir_opcoes():
    num = int(op_entry.get())

    if num < 1 or num > 5:
        result_label.config(text="Número inválido de opções!")
        return

    op_text_entries.clear()

    for widget in op_widgets:
        widget.destroy()
    op_widgets.clear()

    for i in range(num):
        op_text_label = tk.Label(window, text="Opção {}: ".format(i + 1))
        op_text_label.pack()

        op_text_entry = tk.Entry(window)
        op_text_entry.pack()

        op_text_entries.append(op_text_entry)
        op_widgets.append(op_text_label)
        op_widgets.append(op_text_entry)

    confirm_button.config(state=tk.NORMAL)


def escolher_opcao():
    op = [entry.get() for entry in op_text_entries if entry.get()]

    if not op:
        result_label.config(text="Digite pelo menos uma opção!")
        return

    randomnum = random.randint(0, len(op) - 1)

    result_label.config(text="O sistema escolheu a opção: {}".format(op[randomnum]))


# Criação da janela principal
window = tk.Tk()
window.title("Escolher Opção")
window.geometry("300x300")

# Rótulo e campo de entrada para o número de opções
op_label = tk.Label(window, text="Selecione o número de opções (até 5):")
op_label.pack()

op_entry = tk.Entry(window)
op_entry.pack()

# Botão para exibir os campos de entrada para as opções
show_options_button = tk.Button(window, text="Mostrar Opções", command=exibir_opcoes, state=tk.DISABLED)
show_options_button.pack()

# Lista para armazenar os campos de entrada para as opções
op_text_entries = []
op_widgets = []


# Função para verificar a entrada de número de opções
def verificar_num_opcoes(*args):
    num = op_entry.get()
    if num.isdigit() and 1 <= int(num) <= 5:
        show_options_button.config(state=tk.NORMAL)
    else:
        show_options_button.config(state=tk.DISABLED)


# Associa a função verificar_num_opcoes à entrada de número de opções
op_entry.bind('<KeyRelease>', verificar_num_opcoes)

# Botão para confirmar as opções
confirm_button = tk.Button(window, text="Confirmar", command=escolher_opcao, state=tk.DISABLED)
confirm_button.pack()

# Rótulo para exibir o resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Execução da interface
window.mainloop()
