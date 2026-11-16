def masofa(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}
nomlar = list(shaharlar.keys())
eng_uzoq = ""
max_d = 0

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        s1, s2 = nomlar[i], nomlar[j]
        d = masofa(shaharlar[s1], shaharlar[s2])
        print(f"{s1} va {s2}: {d}")
        if d > max_d:
            max_d = d
            eng_uzoq = f"{s1} — {s2}"

print(f"Eng uzoq yo‘nalish: {eng_uzoq} ({max_d})")
