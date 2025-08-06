import cv2
import numpy as np
import time
from PIL import Image
from pynput.mouse import Controller as ControllerMouse, Button, Listener
import pyautogui
import json

mouse = ControllerMouse()

posicaoTeste = [(447, 251), (1473, 969)]


def verificarTamanho(path: str = "teste2.png", posicaoTeste: list = []):
    with Image.open(path) as img:
        largura, altura = img.size
        # print(f"Largura original: {largura}, Altura original: {altura}")

        max_largura = posicaoTeste[1][0] - posicaoTeste[0][0]
        max_altura = posicaoTeste[1][1] - posicaoTeste[0][1]

        if largura > max_largura or altura > max_altura:
            # print("Imagem muito grande, redimensionando...")

            proporcao = min(max_largura / largura, max_altura / altura)
            nova_largura = int(largura * proporcao)
            nova_altura = int(altura * proporcao)

            img = img.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)
            img.save("images/temp_resized.png")

            # print(f"Nova largura: {nova_largura}, Nova altura: {nova_altura}")
            return "images/temp_resized.png"

    return path  # Se já couber, retorna o caminho original


def desenharContorno(path: str = "teste2.png", posicao: list = []):
    # Carregar a imagem
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        # print("Erro ao carregar a imagem.")
        return "Erro ao carregar a imagem."
    # Detectar bordas
    edges = cv2.Canny(image, 100, 200)
    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Mover o mouse ao longo dos contornos
    time.sleep(1)
    for contour in contours:
        for point in contour:
            x, y = point[0]
            mouse.position = (
                posicao[0][0] + x,
                posicao[0][1] + y,
            )
            mouse.press(Button.left)
            time.sleep(0.01)
        mouse.release(button=Button.left)
    return "Desenho concluído!"


def selecionarCaneta():
    while True:
        try:
            img = pyautogui.locateOnScreen("images/caneta.png", confidence=0.8)
            if img is not None:
                x, y = pyautogui.center(img)
                print(f"Imagem encontrada em: {x}, {y}")
                mouse.position = (x, y)
                mouse.click(Button.left)
                print("Caneta selecionada.")
                break
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao verificar local e tamanho: {e}")
            time.sleep(1)


def selecionarBorracha():
    while True:
        try:
            img = pyautogui.locateOnScreen("images/borracha.png", confidence=0.8)
            if img is not None:
                x, y = pyautogui.center(img)
                # print(f"Imagem encontrada em: {x}, {y}")
                mouse.position = (x, y)
                mouse.click(Button.left)
                # print("Borracha selecionada.")
                break
            else:
                time.sleep(1)
        except Exception as e:
            # print(f"Erro ao verificar local e tamanho: {e}")
            time.sleep(1)


def selecionarTamanho(tamanho: int):
    while True:
        try:
            img = pyautogui.locateOnScreen(
                f"images/tamanho{tamanho}.png", confidence=0.8
            )
            if img is not None:
                x, y = pyautogui.center(img)
                print(f"Imagem encontrada em: {x}, {y}")
                mouse.position = (x, y)
                mouse.click(Button.left)
                print(f"Tamanho {tamanho} selecionado.")
                break
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao verificar local e tamanho: {e}")
            time.sleep(1)


def espereClick(local: str = "Centro"):
    print("Clique no local:S", local)
    click_position = None

    def on_click(x, y, button, pressed):
        nonlocal click_position
        if pressed and button == Button.left:
            click_position = (x, y)
            return False  # Encerra o listener

    with Listener(on_click=on_click) as listener:
        listener.join()

    return click_position


def verificarLocalETamanho(path):
    time.sleep(3)
    meioDaImagem = ()
    while True:
        try:
            img = pyautogui.locateOnScreen(path, confidence=0.8)
            if img is not None:
                x, y = pyautogui.center(img)
                # print(f"Imagem encontrada em: {x}, {y}")
                mouse.position = (x, y)
                meioDaImagem = (x, y)
                break
            else:
                # print("Imagem não encontrada, tentando novamente...")
                time.sleep(1)
        except Exception as e:
            # print(f"Erro ao verificar local e tamanho: {e}")
            time.sleep(1)
    time.sleep(1)
    with Image.open(path) as img:
        largura, altura = img.size
        # print(f"Largura: {largura}, Altura: {altura}")
    time.sleep(1)
    mouse.position = (
        meioDaImagem[0] - largura // 2 + 2,
        meioDaImagem[1] - altura // 2 + 2,
    )
    time.sleep(1)
    mouse.position = (
        meioDaImagem[0] + largura // 2 - 2,
        meioDaImagem[1] + altura // 2 - 2,
    )
    return [
        [meioDaImagem[0] - largura // 2, meioDaImagem[1] - altura // 2],
        [meioDaImagem[0] + largura // 2, meioDaImagem[1] + altura // 2],
    ]


def setup(selecao: int):
    with open("data/config.json", "r") as file:
        data = json.load(file)
        caminho = data["gartic"]["caminho"]
        return execute(selecao, caminho)


def execute(selecao: int, imagem: str):
    if selecao == 1:
        posicao = verificarLocalETamanho("images/gartic.png")
        new_path = verificarTamanho(imagem, posicao)
        if new_path:
            selecionarCaneta()
            # selecionarTamanho(1)

            # selecionarBorracha()
            # desenharContorno(imagem, posicao)
            # print("Desenho concluído!")
            return desenharContorno(new_path, posicao)
        else:
            # print("A imagem é muito grande para a área selecionada.")
            return "A imagem é muito grande para a área selecionada."
    elif selecao == 2:
        txt = "Vamos marcar a área de desenho."
        print(txt.center(50, "-"))
        posicoes = []
        posicoes.append(espereClick("Esquerda Superior"))
        posicoes.append(espereClick("Direita Inferior"))
        print("Posições capturadas:", posicoes)
        if verificarTamanho(imagem, posicoes):
            print("Desenhando contorno...")
            desenharContorno(imagem, posicoes)
        else:
            print("A imagem é muito grande para a área selecionada.")
