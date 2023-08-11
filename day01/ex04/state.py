def state():
    import sys
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


    def obter_estado(capital):

        contador = 0
        for x, y in capitais.items():
            if capital == y:
                contador = contador +1
                capital = x
                for w, z in estados.items():
                    if z == capital:
                        capital = w
        if contador == 0:           
            print('Capital não encontrada')
            exit()            
        return capital                
        


    if len(sys.argv) == 2:
        capital = sys.argv[1]
        estado = obter_estado(capital)
        print(estado)

# CHAMADA VIA SHELL
if __name__ == '__main__':
    try:
        state()
    except:
        print('PROGRAMA COM ERRO')
