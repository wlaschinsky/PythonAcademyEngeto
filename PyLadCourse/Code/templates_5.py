#  formatted string literal
# formatovaci retezec sablona
soucet = 3 + 4

print('Součet je', soucet)


# f string 
# do sablony jsou promenne dosazeny primo a hned

y_a = 'á'
osloveni = 'Anežko'
soucet = 3 + 4
podpis = 'Váš Program'

print(f"""
Mil{y_a} {osloveni},
Váš výsledek je {soucet}.

S pozdravem,
{podpis}
""")

# formatovani namisto f stringu
# do sablony se promenne dosazuji pomoci metody format - postupne

sablona = 'Ahoj {jmeno}! Tvoje číslo je {cislo}.'
print(sablona.format(cislo=7, jmeno='Hynku'))
print(sablona.format(cislo=42, jmeno='Viléme'))
print(sablona.format(cislo=3, jmeno='Jarmilo'))


# Oproti formátovacím řetězcům umí format užitečnou zkratku: nepojmenované argumenty dosadí postupně do nepojmenovaných míst v šabloně:

vypis = '{} krát {} je {}'.format(3, 4, 3 * 4)
print(vypis)
