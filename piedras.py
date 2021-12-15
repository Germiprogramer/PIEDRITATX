from random import randint

n = randint(10,20)
NUMERODEPIEDRAS = n
print("el número de piedras iniciales es {}".format(NUMERODEPIEDRAS))

def quitarpiedras(NUMERODEPIEDRAS, n):
    while True:
        piedrasfuera = int(input("ELIGE CUANTAS PIEDRAS QUIERES QUITAR: 2,3 o 5>>> "))
        if piedrasfuera == 2:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 2
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
            break
        elif piedrasfuera == 3:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 3
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
            break
        elif piedrasfuera == 5:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 5
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
            break
        else:
            print("GERMANGILIPOLLAS")
    return NUMERODEPIEDRAS


turno = 0
while True:
    if turno == 0:
        print("Es el turno del jugador 1")
        piedrasfuera = int(input("ELIGE CUANTAS PIEDRAS QUIERES QUITAR: 2,3 o 5>>> "))
        if piedrasfuera == 2:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 2
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 3:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 3
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 5:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 5
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        else:
            print("GERMANGILIPOLLAS")
        turno = 1
    elif turno == 1:
        print("Es el turno del jugador 2")
        piedrasfuera = int(input("ELIGE CUANTAS PIEDRAS QUIERES QUITAR: 2,3 o 5>>> "))
        if piedrasfuera == 2:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 2
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 3:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 3
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 5:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 5
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        else:
            print("GERMANGILIPOLLAS")
        turno = 0




