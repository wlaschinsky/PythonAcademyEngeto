# https://naucse.python.cz/course/pyladies/beginners/variables/
# Description: Vypocet obvodu a obsahu ctverce se zadanou stranou

print("Obsah ctverce se stranou 356 je", 356 * 356, "cm2")
print("Obvod ctverce se stranou 356 je", 4 * 356, "cm")

# pro zmenu strany ctverce zmente cislo 356 na jine

strana = 356
print("Obsah ctverce se stranou", strana, "je", strana * strana, "cm2")
print("Obvod ctverce se stranou", strana, "je", 4 * strana, "cm")

# pouziti funkce input

strana = float(input("Zadejte stranu ctverce: "))
print("Obsah ctverce se stranou", strana, "je", strana * strana, "cm2")
print("Obvod ctverce se stranou", strana, "je", 4 * strana, "cm")

# https://naucse.python.cz/course/pyladies/beginners/comparisons/
# porovnani cisel  podminky

print(1 < 2)

nepravda = 1 == 2
print (nepravda)

strana = float(input("Zadejte stranu ctverce: "))
cislo_je_spravne = 0 < strana
if cislo_je_spravne:
    print("Obsah ctverce se stranou", strana, "je", strana * strana, "cm2")
    print("Obvod ctverce se stranou", strana, "je", 4 * strana, "cm")
else:
    print("Strana musi byt kladne cislo")
print("Konec programu")

# jak pridat podminku na overeni, ze ma user zadat cislo a ne string, co kdyz zada string, nechci aby to spadlo

# podminka bez else - pokud je podminka splnena, provede se kod, pokud ne, tak se nic nestane

cislo = int(input('Zadej číslo, přičtu k němu 3: '))
if cislo == 0:
    print('Jé, to je jednoduché!')
print(cislo, '+ 3 =', cislo + 3)

# podminka s elif - pokud je podminka splnena, provede se kod, pokud ne, tak se provede dalsi podminka, pokud je splnena, provede se kod, pokud ne, tak se provede else

vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('A ze kterépak jsi planety?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: víno, cider, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Pro návštěvy z budoucnosti bohužel nemáme nic v nabídce.')

# zanorena podminka - podminka uvnitr podminky - nested if

stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')

if stastna == 'ano':
    # Tenhle kus kódu se provede, když je "šťastná"
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
else:
    # Tenhle kus kódu se provede, když není "šťastná"
    if bohata == 'ano':
        print('Zkus se víc usmívat!')
    else:
        print('To je mi líto.')


# https://naucse.python.cz/course/pyladies/beginners/and-or/
# and - a, or - nebo

a = float(input("Zadej první stranu obdélníka: "))
b = float(input("Zadej druhou stranu obdélníka: "))

if a <= 0 or b <= 0:
    print("Délka nemůže být záporná!")


# Vylepseny program "bohata" a "stastna" - https://naucse.python.cz/course/pyladies/beginners/and-or/

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano' or stastna_retezec == 'Ano':
    stastna = True
elif stastna_retezec == 'ne' or stastna_retezec == 'Ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano' or bohata_retezec == 'Ano':
    bohata = True
elif bohata_retezec == 'ne' or bohata_retezec == 'Ne':
    bohata = False
else:
    print('Nerozumím!')

if bohata and stastna:
    # Je bohatá a zároveň štǎstná, ta se má.
    print('Gratuluji!')
elif bohata:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')
