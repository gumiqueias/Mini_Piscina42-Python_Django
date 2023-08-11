def passa_pra_dist():

    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    var_dict = {}

    for chave, valor in d:
        if valor in var_dict:
            var_dict[valor] = f"{var_dict[valor]} {chave}"
        else:
            var_dict[valor] = chave

    for key, value in var_dict.items():
        print(key, ' : ', value)


if __name__ == '__main__':
    try:
        passa_pra_dist()
    except:
        print('PROGRAMA COM ERRO')

