ime_prez = input("Unesite ime i prezime studenta: ")

print("Unos ocjena iz 6 predmeta")
print("-"*25)

najveca = 1
najmanja = 5
zbroj_ocjena = 0

for i in range(1,7):
    ocjena = int(input(f"{i}. predmet: "))
    if ocjena > najveca:
        najveca = ocjena
    if ocjena < najmanja:
        najmanja = ocjena
    zbroj_ocjena = zbroj_ocjena + ocjena

prosjek_ocjena = zbroj_ocjena/6

print(f"{ime_prez}: prosjek => {prosjek_ocjena}, najveća ocjena => {najveca}, najmanja ocjena => {najmanja}")
    

