from path import Path


def my_program():
    pasta = Path("pasta_de_saida")
    pasta.mkdir_p()
    caminho_arquivo = pasta / "arquivo_de_saida.txt"

    with caminho_arquivo.open("w") as arquivo:
        arquivo.write("Hello World, this is program in Python!")

    with caminho_arquivo.open("r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)


if __name__ == '__main__':
    try:
        my_program()
    except Exception as e:
        print(e)
