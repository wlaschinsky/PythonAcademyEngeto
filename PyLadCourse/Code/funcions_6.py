# Funkce umožňuje pojmenovat nějaký kousek programu, který se pak dá použít pomocí jména bez detailních znalostí toho, jak to vevnitř funguje.

slovo = input('Zadej slovo: ')
pozice = int(input('Zadej pozici: '))
novy_znak= input('Zadej nový znak: ')

# Funkce se definuje příkazem def, za nějž napíšeš jméno funkce, pak do závorky seznam parametrů, které funkce bere, a pak dvojtečku.
# Potom následuje odsazené tělo funkce – příkazy, které funkce provádí.
# Tělo může začít dokumentačním řetězcem (angl. docstring), který popisuje co funkce dělá. To může být jakýkoli řetězec, ale tradičně se uvozuje třemi uvozovkami (i v případě, že je jen jednořádkový).
# Příkazem return pak můžeš z funkce vrátit nějakou hodnotu.
# Při volání funkce se hodnoty, se kterými funkci zavoláš, přiřadí jednotlivým parametrům. 


def zamen(slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo


print(zamen(slovo, pozice, novy_znak))

# print(nove_slovo)   # Toto nefunguje, protože nové_slovo je definováno jen uvnitř funkce.


def napis_hlasku(nazev, skore):
    """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', 256)
napis_hlasku('Protivníkovo', 5)

# Zkus napsat funkci, která vrátí obsah obdélníka daných rozměrů. Příslušný vzoreček je S = a×b, kde a a b jsou délky stran.

a = int(input('Zadej délku strany a: '))
b = int(input('Zadej délku strany b: '))

def obsah_obdelniku(a, b):
    """Vrátí obsah obdélníka daných rozměrů."""
    return a * b

print('Obsah obdélníka je', obsah_obdelniku(a, b))


def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False

        print('Nerozumím! Odpověz "ano" nebo "ne".')        

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
    
# Stejně jako if nebo break je return příkaz, ne funkce. Kolem „své“ hodnoty nepotřebuje závorky.
# Funkce může mít více return příkazů, ale jakmile se jeden z nich vykoná, funkce skončí a další se nevykonají.
# Speciální příkaz return, který jde použít jenom ve funkcích, vrátí danou návratovou hodnotu ven z funkce a zároveň ukončí provádění funkce.
# Chová se tedy trochu jako break, jen místo cyklu opouští celou funkci.