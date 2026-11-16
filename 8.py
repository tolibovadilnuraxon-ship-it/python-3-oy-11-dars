fayllar = ["Hisobot 2026.pdf", "profil rasmi.jpg",
           "video.mp4", "jadval.xlsx", "diagramma.png"]

yaroqli = []
yaroqsiz = []

for f in fayllar:
    if f.endswith((".pdf", ".jpg", ".png")):
        yaroqli.append(f.replace(" ", "_"))
    else:
        yaroqsiz.append(f)

print("Yaroqli:")
for f in yaroqli:
    print(f)

print("\nYaroqsiz:")
for f in yaroqsiz:
    print(f)
