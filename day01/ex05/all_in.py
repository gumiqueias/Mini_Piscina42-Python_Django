def all():
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


    def detectar_tipo(expressao):


        # expressao = expressao.filter(None, expressao)

        if len(expressao) > 2:

            expressao = expressao.title().strip()


            x = valida_capital(expressao)
            y = valida_estados(expressao)

            z = x + y
            
            if (z == 2):
                print(expressao, 'não é uma cidade capital nem um estado')


    def valida_capital(expressao):

        if expressao in capitais.values():
            for estado, capital in capitais.items():
                if expressao == capital:
                    codigo_capital = estado
                    for x, y in estados.items():
                        if codigo_capital == y:
                            print(expressao, 'é a capital de ', x)
                            return 0

        else:
            return 1


    def valida_estados(expressao):

        if expressao in estados:
            for estado, capital in estados.items():
                if expressao == estado:
                    codigo_estado = capital
                    for x, y in capitais.items():
                        if codigo_estado == x:
                            print(y, ' é a capital de ', expressao)
                            return 0

        else:
            return 1


    def all_in(expressoes):
        expressions_list = expressoes.split(",")

        if len(expressions_list) == 1:
            result = detectar_tipo(expressions_list[0])
            if result:
                print(result)
        elif len(expressions_list) > 1:
            for expression in expressions_list:
                result = detectar_tipo(expression)
                if result:
                    print(result)


    if len(sys.argv) == 2:
        expressoes = sys.argv[1]
        all_in(expressoes)


# CHAMADA VIA SHELL
if __name__ == '__main__':

    try:
        all()
    except:
        print('PROGRAMA COM ERRO')


  