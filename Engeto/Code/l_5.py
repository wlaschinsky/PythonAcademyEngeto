# TODO promenne
sklad = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""

oddelovac = '=' * 40

#--------------------------------------------

# TODO kosik = dict()

kosik = {}


# TODO Pozdrav a vypsani nabidky
print('Vitejte v nasi prodejne.')
print(oddelovac)
print(nabidka)
print(oddelovac)
print("Pro konceni napis 'konec'")

# TODO cely cyklus

while True:
    zbozi = input('Zadej zbozi: ')
    if zbozi != 'konec':
        break
print(zbozi)

    
    # TODO pokud zbozi nebude v nabidce

    # TODO Pokud vybrane zbozi neni v nakupnim kosiku

    # TODO pokud zbozi je v kosiku

    # TODO pokud zbozi jiz neni skladem

# TODO vypis kosiku

