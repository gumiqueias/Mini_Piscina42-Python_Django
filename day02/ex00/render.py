import sys
import os
import re


def carregar_configuracoes():
    configuracoes = {}
    with open("settings.py") as f:
        exec(f.read(), configuracoes)
    return configuracoes


def renderizar_template(arquivo_template, configuracoes):
    with open(arquivo_template) as f:
        conteudo_template = f.read()

    for chave, valor in configuracoes.items():
        conteudo_template = re.sub(
            r"{" + chave + r"}", str(valor), conteudo_template)

    return conteudo_template


def salvar_em_html(conteudo_html):
    with open("file.html", "w") as f:
        f.write(conteudo_html)


if __name__ == '__main__':

    try:

        if len(sys.argv) != 2:
            print("Uso: python3 render.py <arquivo_template>")
            sys.exit(1)

        arquivo_template = sys.argv[1]
        if not arquivo_template.endswith(".template"):
            print(
                "Erro: Extensão de arquivo inválida. O arquivo de template deve ter a extensão .template.")
            sys.exit(1)

        if not os.path.exists(arquivo_template):
            print("Erro: O arquivo de template especificado não existe.")
            sys.exit(1)

        configuracoes = carregar_configuracoes()
        conteudo_html = renderizar_template(arquivo_template, configuracoes)
        salvar_em_html(conteudo_html)

    except Exception as e:
        print(e)
