from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def comecar_contar():
    contar = 0
    segundos_correndo(contar)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
''' FURADA PQ A GUI É EVENT DRIVEN
def rodar_tempo():
    tempo = 0
    while tempo != 60
        time.sleep(1)
        tempo+= 1
'''
def segundos_correndo(contar_segundos):
    canvas.itemconfig(timer_text, text=count)
    if contar_segundos == 60:
        contar_segundos = 0
    else:
        janela.after(1000, segundos_correndo, contar_segundos += 1)
        
        

# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title("Pomodoro")
janela.config(padx=100, pady=50, bg=YELLOW)
#----
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#label
texto = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
texto.grid(row=0, column=1)

#botoes
botao_start = Button(text="Começar", highlightthickness=0, command=comecar_contar)
botao_start.grid(row=2, column=0)


botao_reset = Button(text="Resetar", highlightthickness=0)
botao_reset.grid(row=2, column=2)

#joinha
texto = Label(text="✓", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
texto.grid(row=3, column=1)

janela.mainloop()