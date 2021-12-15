from random import randint

n = randint(10,20)
NUMERODEPIEDRAS = n
print("el número de piedras iniciales es {}".format(NUMERODEPIEDRAS))




turno = "jugador1"
while NUMERODEPIEDRAS > 0:
    if turno == "jugador1":
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
            turno = "jugador1"
        turno = "jugador2"
    elif turno == "jugador2":
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
            turno = "jugador2"
        turno = "jugador1"

if NUMERODEPIEDRAS <= 1 and turno == "jugador2":
    print("Ha ganado el jugador 1")
elif NUMERODEPIEDRAS <= 1 and turno == "jugador1":
    print("Ha ganado el jugador 2")