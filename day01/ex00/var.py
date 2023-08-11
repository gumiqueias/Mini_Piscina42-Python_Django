def minha_var():
    nome = "42"
    idade = 42
    aluno42 = True
    altura = "quarante-deux"
    flot = 42.0
    complexo = 4+2j
    notas = [42]
    pontos = (42,)
    peso = {42:42}
    seta = set()
    
    print(idade, ' has a type ',type(idade))
    print(nome, ' has a type ',type(nome))
    print(altura, ' has a type ',type(altura))
    print(flot, ' has a type ',type(flot))
    print(aluno42, ' has a type ',type(aluno42))
    print(notas, ' has a type ',type(notas))
    print(peso, ' has a type ',type(peso))
    print(pontos, ' has a type ',type(pontos))
    print(seta, ' has a type ',type(seta))

if __name__=='__main__':
    try:
        minha_var()    
    except:
        print('PROGRAMA COM ERRO')
