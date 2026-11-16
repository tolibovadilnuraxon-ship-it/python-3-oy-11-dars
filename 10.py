jami = 0
max_soat = 0
max_ism = ""

with open("ish_vaqti.txt", "r") as f:
    for qator in f:
        ism, soat = qator.split()
        if soat.isdigit():
            soat = int(soat)
            jami += soat
            if soat > max_soat:
                max_soat = soat
                max_ism = ism
        else:
            print(f"Ogohlantirish: {ism} uchun soat qiymati noto‘g‘ri.")

print("Jami ish soati:", jami)
print(f"Eng ko‘p ishlagan: {max_ism} — {max_soat} soat")
