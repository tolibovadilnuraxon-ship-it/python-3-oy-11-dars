buyurtmalar = [
    {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
    {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
    {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1}
]

eng_qimmat = ""
max_summa = 0

for b in buyurtmalar:
    summa = b["narx"] * b["miqdor"]
    print(f"{b['mahsulot']}: {summa} so‘m")
    if summa > max_summa:
        max_summa = summa
        eng_qimmat = b["mahsulot"]

print(f"Eng qimmat buyurtma: {eng_qimmat} — {max_summa} so‘m")
