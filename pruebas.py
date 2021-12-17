from random import randint
NUMERODEPIEDRAS = 5
piedrasfuera = 0

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

print(piedrasfuera)