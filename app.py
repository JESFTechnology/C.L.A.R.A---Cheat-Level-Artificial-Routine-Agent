import tkinter as tk
from tkinter import messagebox, filedialog
from time import sleep
from PIL import Image, ImageTk

# Importando módulos internos
from src.save import salvarGarticConfigImage
from src.desenhar import setup

# --- Cores & Estilo Hacker ---
COR_FUNDO = "#000000"  # Preto
COR_TEXTO = "#ff1a1a"  # Vermelho sangue
FONTE = ("Courier New", 12, "bold")


# --- Funções ---
def selecionar_jogo():
    janela.geometry("500x200")
    jogo_selecionado = jogo_var.get()
    if jogo_selecionado == "Gartic":
        mostrar_botoes_gartic()
    else:
        esconder_botoes_gartic()


def mostrar_botoes_gartic():
    botao_selecionar_imagem.pack(pady=5)
    botao_iniciar.pack(pady=5)
    # Cria um rótulo para exibir a imagem
    rotulo_imagem.pack()
    atualizar_imagem("images/selected_image.png")  # Imagem padrão ao abrir o jogo


def esconder_botoes_gartic():
    botao_selecionar_imagem.pack_forget()
    botao_iniciar.pack_forget()
    rotulo_imagem.pack_forget()


def selecionar_imagem():
    arquivo_imagem = filedialog.askopenfilename(
        title="Selecionar Imagem", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    if arquivo_imagem:
        salvarGarticConfigImage(arquivo_imagem)
        atualizar_imagem(arquivo_imagem)


def atualizar_imagem(arquivo_imagem):
    try:
        imagem = Image.open(arquivo_imagem)
        # Ajusta a imagem para ter no máximo 300px de largura
        largura_maxima = 300
        largura, altura = imagem.size
        if altura > 200:
            novaAlturaTela = 400+altura
            janela.geometry(f"500x{novaAlturaTela}")
        if largura > largura_maxima:
            proporcao = largura_maxima / largura
            nova_largura = largura_maxima
            nova_altura = int(altura * proporcao)
            imagem = imagem.resize(
                (nova_largura, nova_altura), Image.Resampling.LANCZOS
            )
        imagem.save("images/selected_image.png")
        # Converte a imagem para um formato que o tkinter pode usar
        imagem_tk = ImageTk.PhotoImage(imagem)
        # Atualiza o rótulo com a nova imagem
        rotulo_imagem.config(image=imagem_tk)
        rotulo_imagem.image = imagem_tk  # Mantém uma referência da imagem
    except Exception as e:
        pass


def iniciar_jogo():
    sleep(2)
    msg = setup(1)
    messagebox.showinfo("Aviso", msg)


# --- Janela Principal ---
janela = tk.Tk()
janela.title("CLARA.EXE - Boot do Sistema")
janela.geometry("500x200")
janela.config(bg=COR_FUNDO)
janela.iconphoto(janela, tk.PhotoImage(file="images/icon.png"))

# --- Componentes Visuais ---
mensagem = tk.Label(
    janela,
    text="Olá, querido(a). Vamos trapacear?",
    fg=COR_TEXTO,
    bg=COR_FUNDO,
    font=FONTE,
)
mensagem.pack(pady=15)

jogo_var = tk.StringVar(value="Gartic")

menu_jogos = tk.OptionMenu(janela, jogo_var, "Gartic", "Roblox", "Minecraft")
menu_jogos.config(
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    font=FONTE,
    activebackground=COR_TEXTO,
    activeforeground=COR_FUNDO,
    highlightbackground=COR_TEXTO,
)
menu_jogos["menu"].config(bg=COR_FUNDO, fg=COR_TEXTO, font=FONTE)
menu_jogos.pack(pady=10)

rotulo_imagem = tk.Label(janela)

botao_selecionar = tk.Button(
    janela,
    text="Selecionar Jogo",
    command=selecionar_jogo,
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    font=FONTE,
    activebackground=COR_TEXTO,
    activeforeground=COR_FUNDO,
    highlightbackground=COR_TEXTO,
)
botao_selecionar.pack(pady=10)

botao_selecionar_imagem = tk.Button(
    janela,
    text="Selecionar Imagem",
    command=selecionar_imagem,
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    font=FONTE,
    activebackground=COR_TEXTO,
    activeforeground=COR_FUNDO,
    highlightbackground=COR_TEXTO,
)

botao_iniciar = tk.Button(
    janela,
    text="Iniciar Desenho",
    command=iniciar_jogo,
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    font=FONTE,
    activebackground=COR_TEXTO,
    activeforeground=COR_FUNDO,
    highlightbackground=COR_TEXTO,
)

# Loop final
janela.mainloop()
