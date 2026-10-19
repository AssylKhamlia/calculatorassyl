while True:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))

    if b == 0:
        print("Erreur : division par zéro impossible.")
    else:
        print(f"{a} / {b} = {a / b:.2f}")
