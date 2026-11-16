def bolish(a, b):
    assert type(a) in (int, float) and type(b) in (int, float)
    return a / b

try:
    son1 = float(input("Birinchi son: "))
    son2 = float(input("Ikkinchi son: "))
    print("Natija:", bolish(son1, son2))
except ValueError:
    print("Xatolik: Faqat son kiriting.")
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas.")
except AssertionError:
    print("Xatolik: Tur mos emas.")

print("Dastur ishlashda davom etmoqda.")
