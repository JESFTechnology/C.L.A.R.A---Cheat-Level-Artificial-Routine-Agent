import json


def salvarGarticConfigImage(caminho: str):
    try:
        with open("data/config.json", "r") as file:
            json_data = json.load(file)
        json_data["gartic"]["caminho"] = caminho
        with open("data/config.json", "w") as file:
            json.dump(json_data, file, indent=4)
            # print("Configuração do Gartic atualizada com sucesso.")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo com o caminho
        with open("data/config.json", "w") as file:
            json_data = {"gartic": {"caminho": ""}}
            json.dump(json_data, file, indent=4)
            # print("Arquivo gartic.json criado com o caminho fornecido.")


def setup():
    pass
