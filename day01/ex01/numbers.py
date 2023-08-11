def busca_txt():

    arq = open("numbers.txt")
    dados = arq.read()

    return dados


def separa_dados(dados):

    dados = dados.split(",")

    for dado in dados:
        print(dado)


# CHAMADA VIA SHELL
if __name__ == '__main__':
    try:
        separa_dados(busca_txt()) 
    except:
        print('PROGRAMA COM ERRO')
