tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

barchasi = tadbir_1 & tadbir_2 & tadbir_3
kamida_2 = (tadbir_1 & tadbir_2) | (tadbir_2 & tadbir_3) | (tadbir_1 & tadbir_3)
faqat_1 = (tadbir_1 | tadbir_2 | tadbir_3) - kamida_2

print("Barcha tadbirlarda:", ", ".join(barchasi))
print("Faqat bitta tadbirda:", ", ".join(faqat_1))
print("Kamida ikkita tadbirda:", ", ".join(kamida_2))
