count = 0

br = int(input("Unesite prirodan broj: "))
while br <= 0:
    br = int(input("Unesite prirodan broj: "))

print(f"Djelitelji broja {br} su:", end = " ")

for i in range(1, br+1):
    if br%i == 0:
        print(i, end = " ")
        count = count + 1

print()

print(f"Broj {br} ima {count} djelitelja.")