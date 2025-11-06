def areaRettangolo(base, altezza):
    if base == 0:
        print("Il lato non può essere 0")
    else:
       area = (base * altezza)
       print(f"L'area del rettangolo è {area}")

areaRettangolo(0, 12)