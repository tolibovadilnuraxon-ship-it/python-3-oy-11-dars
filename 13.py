import csv

yonalish = input("Yo‘nalish: ")
topilganlar = []

with open("talabalar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ustunlar = reader.fieldnames
    for row in reader:
        if row["yonalish"] == yonalish:
            topilganlar.append(row)

topilganlar.sort(key=lambda x: int(x["ball"]), reverse=True)

with open("filtrlangan_talabalar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=ustunlar)
    writer.writeheader()
    writer.writerows(topilganlar)

print(f"{len(topilganlar)} ta talaba topildi.")
print("Natijalar filtrlangan_talabalar.csv fayliga yozildi.")
