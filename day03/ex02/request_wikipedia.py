import requests
import json
import dewiki
import sys


def request_wikipeadia(page: str):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": page,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        res = requests.get(url=URL, params=PARAMS)
        res.raise_for_status()
    except requests.HTTPError as e:
        raise e
    try:
        data = json.loads(res.text)
        print(data)
    except json.decoder.JSONDecodeError as e:
        raise e
    if data.get("error") is not None:
        raise Exception(data["error"]["info"])
    return (dewiki.from_string(data["parse"]["wikitext"]["*"]))


def my_program():
    if (len(sys.argv) == 2):
        try:
            wiki_data = request_wikipeadia(sys.argv[1])
        except Exception as e:
            return print(e)
        try:
            f = open("{}.wiki".format(sys.argv[1]), "w")
            f.write(wiki_data)
            f.close
        except Exception as e:
            return print(e)
    elif len(sys.argv) == 2:
        print("DIGITE SOMENTE 1 ARGUMENTO!!")
    else:
        print("CONTAGEM DE ARGUMENTOS INCORRETA")


if __name__ == '__main__':
    try:
        my_program()
    except Exception as e:
        print("PROGRAMA COM ERRO", e)
