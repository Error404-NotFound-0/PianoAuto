import subprocess
import sys
import importlib

def garantir_bibliotecas(*pacotes):
    for pacote in pacotes:
        try:
            importlib.import_module(pacote)
        except ImportError:
            print(f"'{pacote}' não encontrado. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
        
            # Força o Python a reconhecer a nova instalação sem precisar fechar o programa
            importlib.invalidate_caches()

# Garante a instalação
garantir_bibliotecas("pyautogui")


import tkinter as tk
import pyautogui as pg
import time

pg.PAUSE = 0.05
# lógica
def iniciar():
    time.sleep(2)
    acorde = []
    dentro_acorde = False
    partitura = entrada_partitura.get()
    pausa = entrada_pausa.get()
    for i in partitura:
        if i == ' ' or i == '\n':
            pg.sleep(pausa)
            continue
        elif i == '[':
            dentro_acorde = True
            continue
        elif i == ']':
            pg.hotkey(*acorde)
            acorde = []
            dentro_acorde = False
            continue
        elif dentro_acorde == True:
            acorde.append(i)
        else:
            pg.press(i)
    exit



# interface
janela = tk.Tk()
janela.geometry('250x250')
texto_partitura = tk.Label(janela, text='Coloque a partitura aqui abaixo:')
texto_partitura.pack(pady=5)
entrada_partitura = tk.Entry(janela)
entrada_partitura.pack(pady=10)
texto_pausa = tk.Label(janela, text='Coloque o valor da pausa aqui abaixo:')
texto_pausa.pack(pady=5)
entrada_pausa = tk.Entry(janela)
entrada_pausa.pack(pady=10)
botao_iniciar = tk.Button(janela, text='Iniciar', command=iniciar)
botao_iniciar.pack(pady=10)
janela.mainloop()

