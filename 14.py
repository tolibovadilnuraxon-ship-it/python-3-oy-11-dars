import matplotlib.pyplot as plt

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]

buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(oylar, daromad, marker="o")
plt.title("Oylik daromad dinamikasi")
plt.xlabel("Oylar")
plt.ylabel("Daromad (mln so‘m)")

plt.subplot(1, 3, 2)
plt.bar(kategoriyalar, savdo)
plt.title("Kategoriyalar savdosi")
plt.xlabel("Kategoriyalar")
plt.ylabel("Savdo (dona)")

plt.subplot(1, 3, 3)
plt.hist(buyurtma_qiymatlari, bins=5, edgecolor="black")
plt.title("Buyurtma qiymatlari taqsimoti")
plt.xlabel("Qiymat")
plt.ylabel("Soni")

plt.tight_layout()
plt.show()
