natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = [x["ism"] for x in filter(lambda x: x["ball"] > 70, natijalar)]
oshirilgan = list(map(lambda x: round(x["ball"] * 1.1, 1), natijalar))
saralangan = [x["ism"] for x in sorted(natijalar, key=lambda x: x["ball"], reverse=True)]

print("70 dan yuqori:", ", ".join(yuqori))
print("10% oshirilgan ballar:", oshirilgan)
print("Saralangan:", ", ".join(saralangan))
