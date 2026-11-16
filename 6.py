menu = {"lavash": 28000, "somsa": 10000, "choy": 5000}

def buyurtma(*args, **kwargs):
    jami = 0
    for ovqat in args:
        if ovqat in menu:
            jami += menu[ovqat]
        else:
            print(f"Ogohlantirish: {ovqat} menyuda yo‘q")
            
    for k, v in kwargs.items():
        print(f"{k.capitalize()}: {v}")
    print(f"Jami: {jami} so‘m")

buyurtma("lavash", "choy", "somsa", mijoz="Dilshod", telefon="901234567")
