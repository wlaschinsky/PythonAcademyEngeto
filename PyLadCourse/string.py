# retezce
# program, ktery se zepta na slovo, pozici a pismeno a na teto pozici pismeno vymeni
# program zameni pismeno ve slove

slovo = input('Slovo: ')
pozice = int(input('Které písmeno zaměnit? '))
novy_znak = input('Nové písmeno: ')

nove_slovo = slovo[:pozice-1] + novy_znak + slovo[pozice:]

# ekvivalent z python kurzu
# zacatek_slova = slovo[:pozice]
# konec_slova = slovo[pozice + 1:]
# nove_slovo = zacatek_slova + novy_znak + konec_slova

print(nove_slovo)

