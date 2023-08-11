

class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, nome="My name? I’m nobody, an intern, I have no name."):
        self.nome = nome

    def __str__(self):
        return self.nome

    def trabalhar(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def fazer_cafe(self):
        return Intern().Coffee()


def test():
    estagiario_no_name = Intern()
    print(estagiario_no_name)

    estagiario_com_nome_mark = Intern("Mark")
    print(estagiario_com_nome_mark)

    cafe = estagiario_com_nome_mark.fazer_cafe()
    print(cafe)

    return estagiario_no_name


if __name__ == '__main__':

    estagiario_sem_nome = test()

    try:
        estagiario_sem_nome.trabalhar()
    except Exception as e:
        print(e)
