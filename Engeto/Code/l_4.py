slovnik = {"klic": "hodnota"}
slovnik["klic2"] = "hodnota2"
# co bude vysledkem? #1
print(slovnik["klic2"])

slovnik["klic"] = "hodnota2"
# co bude vysledkem? #2
print(slovnik.get("klic2"))

# co bude vysledkem? #3
print(slovnik.get("klic", "sefeffs"))