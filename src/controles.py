from pynput.keyboard import Controller as ControllerKeyboard, Key
from pynput.mouse import Controller as ControllerMouse, Button
from time import sleep

from math import cos, sin
from PIL import Image
import pyautogui

teclado = ControllerKeyboard()
mouse = ControllerMouse()


def gravarMovimento():
    """
    Grava o movimento de um item no sistema.
    """
    # Implementação da função para gravar o movimento
    pass


def gravarMovimentoItem():
    """
    Grava o movimento de um item específico no sistema.
    """
    # Implementação da função para gravar o movimento de um item
    pass


def executarMovimento():
    """
    Executa o movimento de um item no sistema.
    """
    # Implementação da função para executar o movimento
    pass


def executarMovimentoItem():
    """
    Executa o movimento de um item específico no sistema.
    """
    # Implementação da função para executar o movimento de um item
    pass


def puloCronometrado(tempo: int):
    teclado.press(Key.space)
    sleep(1)
    teclado.release(Key.space)
    sleep(tempo)


def controleMouse(x: int, y: int):
    """
    Controla o mouse para mover para uma posição específica.

    :param x: Coordenada X para mover o mouse.
    :param y: Coordenada Y para mover o mouse.
    """
    mouse.position = (x, y)
    sleep(0.1)  # Pequena pausa para garantir que o movimento seja registrado


def moverMouse(x: int, y: int):
    mouse.move(x, y)
    sleep(0.1)  # Pequena pausa para garantir que o movimento seja registrado


def moverMouseMeio(x: int, y: int):
    x, y = x // 2, y // 2
    x, y = (767, 425)
    # print(f"Movendo mouse para o meio: ({x}, {y})")
    mouse.position = (x, y)
    sleep(1)  # Pequena pausa para garantir que o movimento seja registrado


def moverDireita(x: int):
    for i in range(0, x, 1):
        # print(f"Movendo mouse para a direita: {i}")
        mouse.move(1, 0)
        sleep(0.01)


def moverEsquerda(x: int):
    for i in range(x, 0, -1):
        # print(f"Movendo mouse para a esquerda: {i}")
        mouse.move(-1, 0)
        sleep(0.01)


def moverCima(y: int):
    for i in range(0, y, 1):
        # print(f"Movendo mouse para cima: {i}")
        mouse.move(0, -1)
        sleep(0.01)


def moverBaixo(y: int):
    for i in range(y, 0, -1):
        # print(f"Movendo mouse para baixo: {i}")
        mouse.move(0, 1)
        sleep(0.01)


def moverMouseSuave(x: int, y: int, isClick: bool = False):
    ax, ay = mouse.position
    for i in range(ax, x):
        mouse.position(x, ay)
        sleep(0.1)
    for i in range(ay, y):
        mouse.position(x, y)
        sleep(0.1)


def lerMovimento():
    print(mouse.position)
    return mouse.position


def fazerCirculo(x: int, y: int, raio: int):
    """
    Faz um movimento circular com o mouse.

    :param x: Coordenada X do centro do círculo.
    :param y: Coordenada Y do centro do círculo.
    :param raio: Raio do círculo.
    """
    x, y = (767, 425)
    for angle in range(0, 360, 1):
        rad = angle * (3.14159 / 180)  # Convertendo graus para radianos
        new_x = int(x + raio * cos(rad))
        new_y = int(y + raio * sin(rad))
        mouse.position = (new_x, new_y)
        mouse.click(Button.left)
        sleep(0.01)  # Pequena pausa para suavizar o movimento


def selecionarCaneta():
    # Carregar a imagem
    try:
        img = "paint_images/canetaPaint.png"
        img = pyautogui.locateOnScreen(img, confidence=0.8)
        # Verificar se a imagem foi encontrada
        if img:
            x, y = pyautogui.center(img)
            mouse.position = (x, y)
            sleep(1)
            mouse.click(button=Button.left)
    except Exception as e:
        print(f"Erro ao selecionar caneta: {e}")


def selecionarBorracha():
    # Carregar a imagem
    try:
        img = "paint_images/borrachaPaint.png"
        img = pyautogui.locateOnScreen(img, confidence=0.8)
        # Verificar se a imagem foi encontrada
        if img:
            x, y = pyautogui.center(img)
            mouse.position = (x, y)
            sleep(1)
            mouse.click(button=Button.left)
    except Exception as e:
        print(f"Erro ao selecionar caneta: {e}")


def aumentarCaneta(px: int = 50):
    # Carregar a imagem
    try:
        img = "paint_images/scrollCaneta.png"
        img = pyautogui.locateOnScreen(img, confidence=0.8)
        # Verificar se a imagem foi encontrada
        if img:
            x, y = pyautogui.center(img)
            mouse.position = (x, y)
            moverBaixo(240)
            sleep(1)
            mouse.click(button=Button.left)
            moverCima(px)
            mouse.click(button=Button.left)
            sleep(1)

    except Exception as e:
        print(f"Erro ao aumentar caneta: {e}")


def teste():
    selecionarCaneta()
    aumentarCaneta()
    moverMouseMeio(0, 0)
    fazerCirculo(0, 0, 100)
    fazerCirculo(0, 0, 75)
    fazerCirculo(0, 0, 50)
    fazerCirculo(0, 0, 25)
    selecionarBorracha()
    fazerCirculo(0, 0, 100)
    fazerCirculo(0, 0, 75)
    fazerCirculo(0, 0, 50)
    fazerCirculo(0, 0, 25)


def setup(x: int = 1680, y: int = 1024):
    sleep(5)
    # moverMouseMeio(x, y)
    # moverDireita(30)
    # moverEsquerda(60)
    # moverDireita(30)
    # sleep(1)
    teste()


setup()
