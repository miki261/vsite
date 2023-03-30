from math import sqrt

a = int(input("Koeficijent A kvad. jedn. : "))
if a == 0:
    print("Ovo nije kvadratna jednadžba.")
elif a != 0:
    b = int(input("Koeficijent B kvad. jedn. : "))
    c = int(input("Koeficijent C kvad. jedn. : "))
    diskriminanta = (b**2)-(4*a*c)
    if diskriminanta > 0:
        rezultat1 = (-b+sqrt(diskriminanta))/(2*a)
        rezultat2 = (-b-sqrt(diskriminanta))/(2*a)
        print(f"""Rješenja:
        x1 = {rezultat1}
        x2 = {rezultat2}
        D = {diskriminanta}""")
    elif diskriminanta == 0:
        rezultat = (-b)/(2*a)
        print(f"""Rješenje:
        x = {rezultat}
        D = {diskriminanta}""")
    else:
        print("Nema realnih rješenja.")