# funkce delka retezce

print(len("anakonda"))

# funkce porovnavani in, not in 

print("coko" in "anakonda")

# Metoda (angl. method) je jako funkce – něco, co se dá zavolat. Na rozdíl od funkce je svázaná s nějakým objektem (hodnotou). 
#Volá se tak, že se za objekt napíše tečka, za ní jméno metody a za to celé se, jako u funkcí, připojí závorky s případnými argumenty.

retezec = 'Ahoj'
print(retezec.upper())
print(retezec.lower())
print(retezec)


# Pro procvičení metod a vybírání znaků si zkus napsat program, který se zeptá na jméno, pak na příjmení a pak vypíše iniciály – první písmena zadaných jmen.

jmeno = input('Jméno: ').upper()  
prijmeni = input('Příjmení: ').upper()
print ("Tvoje iniciály jsou: "+ jmeno[0] + prijmeni[0])

# preferovany zpusob

# jmeno = input('Zadej jméno: ')
# prijmeni = input('Zadej příjmení ')
# print('Iniciály:', (jmeno[0] + prijmeni[0]).upper())

# jmeno = input('Zadej jméno: ')
# prijmeni = input('Zadej příjmení ')
# inicialy = jmeno[0] + prijmeni[0]
# print('Iniciály:', inicialy.upper())

