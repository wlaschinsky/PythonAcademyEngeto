# importy zakladnich knihoven (modulu)
import random

# importy vlastnich modulu
import grafika
import slova
# from slova import hadana_slova   # muzu pouzit primo hadana_slova

# var

zivot  = 7
hra_bezi = True # prepnu na false jakmile bude konec
random.seed(2)
slovo = random.choice(slova.hadana_slova)
tajenka = ["_"] * len(slovo)

# TODO hlavni smycka hry
while zivot > 0 and hra_bezi:   # kdyz neporovnavam tak nemusim psat == True, vzdycky je to brane jako True 
     
    # TODO zobraz tajenku
    print("".join(tajenka))           #prazdny string - join hodnot v kulate zavorce
   
    # TODO input
    hadani = input("Napis pismeno nebo slovo: ")
    
    # TODO pokud uzivatel uhadl cele slovo
    if tajenka == slovo:
        print ("Good job")
        hra_bezi = False

    # TODO pokud uzivatel uhadne pismeno
    elif len(hadani) == 1 and hadani in slovo: 
        for poradi, pismeno in enumerate(slovo):
            if pismeno == hadani and tajenka[poradi] == "_":
                tajenka[poradi] = hadani
        if "_" not in tajenka:
            print("Vyborne, slovo je: ", slovo)
            hra_bezi = False
            print("Zbyva ti", zivot, "zivotu.")
        else:
            hra_bezi = True
            print("Zbyva ti", zivot, "zivotu.")
    
    # TODO pokud uzivatel uhadl spatne pismeno

# TODO vypis else po tom, co je while cyklus prerusen



# vypisovat pocet zivotu po kazdem ubrani 
# pridat grafiku
# random zvoleni slova
# pokud v prubehu doplnim slovo cele, ne po pismenu - vyhodnotit, ze jsem vyhral
