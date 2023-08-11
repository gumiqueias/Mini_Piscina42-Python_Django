import sys
import antigravity


def calcula_geohash(x, y, z):

    return antigravity.geohash(x, y, z)


def separa_arg():

    if len(sys.argv) == 4:
        latitude = ''
        longitude = ''
        for i in range(1, 4):
            try:
                if not isinstance(latitude, float):
                    latitude = float(sys.argv[i])
                elif not isinstance(longitude, float):
                    longitude = float(sys.argv[i])
                else:
                    text = bytes(sys.argv[i], 'utf-8')
            except:
                text = bytes(sys.argv[i], 'utf-8')

        calcula_geohash(latitude, longitude, text)
    else:
        print("Paramêtros inválidos")
        sys.exit(1)


if __name__ == '__main__':
    try:
        separa_arg()
    except Exception as e:
        print(e)
