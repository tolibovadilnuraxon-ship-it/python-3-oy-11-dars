import csv

tushum = {}

with open("savdo.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        kat = row["kategoriya"]
        summa = int(row["narx"]) * int(row["miqdor"])
        tushum[kat] = tushum.get(kat, 0) + summa

for k, v in tushum.items():
    print(f"{k}: {v:,}".replace(",", " ") + " so‘m")

eng_kop = max(tushum, key=tushum.get)
print("Eng daromadli kategoriya:", eng_kop)
