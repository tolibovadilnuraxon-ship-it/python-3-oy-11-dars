ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

natija = ombor_1.copy()
for k, v in ombor_2.items():
    natija[k] = natija.get(k, 0) + v

print(natija)
