from random import randint

n = randint(10,20)
NUMERODEPIEDRAS = n
print("el número de piedras iniciales es {}".format(NUMERODEPIEDRAS))
piedrasfuera=0

def accionIA(NUMERODEPIEDRAS, piedrasfuera):
    if NUMERODEPIEDRAS == 2:
        piedrasfuera = 2
    elif NUMERODEPIEDRAS == 3:
        piedrasfuera = 3
    elif NUMERODEPIEDRAS == 4:
        piedrasfuera = 3
    elif NUMERODEPIEDRAS == 5:
        piedrasfuera = 5
    elif NUMERODEPIEDRAS == 6:
        piedrasfuera = 5
    elif NUMERODEPIEDRAS >= 7:
         while True:
            piedrasfuera = randint(2,5)
            if piedrasfuera == 4:
                pass
            else:
                break
    return piedrasfuera
        
turno = "jugador1"
while NUMERODEPIEDRAS > 1:
    if turno == "jugador1":
        print("Es el turno del jugador 1")
        piedrasfuera = accionIA(NUMERODEPIEDRAS,piedrasfuera)
        if piedrasfuera == 2:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 2
            print("Se retiran 2 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 3:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 3
            print("Se retiran 3 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 5:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 5
            print("Se retiran 5 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        turno = "jugador2"
    elif turno == "jugador2":
        print("Es el turno del jugador 2")
        piedrasfuera = accionIA(NUMERODEPIEDRAS,piedrasfuera)
        if piedrasfuera == 2:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 2
            print("Se retiran 2 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 3:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 3
            print("Se retiran 3 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        elif piedrasfuera == 5:
            NUMERODEPIEDRAS = NUMERODEPIEDRAS - 5
            print("Se retiran 5 piedras")
            print("Tenemos {} piedras".format(NUMERODEPIEDRAS))
        turno = "jugador1"

if NUMERODEPIEDRAS <= 1 and turno == "jugador2":
    print("No se pueden realizar más movimientos, ha ganado el jugador 1")
elif NUMERODEPIEDRAS <= 1 and turno == "jugador1":
    print("No se pueden realizar más movimientos, ha ganado el jugador 2")