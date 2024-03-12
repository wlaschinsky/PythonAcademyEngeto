muj_druhy_slovnik = dict(klic="hodnota")
muj_druhy_slovnik["novy klic"] = "nova_hodnota"
muj_druhy_slovnik["klic"]
print(muj_druhy_slovnik["klic"])


device = {
    "platform": "android",
    "type": {
        "model": "Galaxy S10",
        "year": 2019,
    },
    "name": "Samsung",
    "version": ["10", "11", "12"],
}


value = device["version"]
if  0 < len(device["version"])

print(value[0])