def capital():
    estados = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capitais = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    import sys

    def obter_capital(estado):
        if estado in estados:
            codigo_estado = estados[estado]
            if codigo_estado in capitais:
                return capitais[codigo_estado]
        return "Estado desconhecido"
    
    

    if len(sys.argv) == 2:
        estado = sys.argv[1]
        capital = obter_capital(estado)
        print(capital)



# CHAMADA VIA SHELL
if __name__ == '__main__':

    try:
        capital()
    except:
        print('PROGRAMA COM ERRO')
