count = 0
red = 1
for i in range(1, 1001):
    if i % 12 == 0 and i % 7 != 0:
        print(i, end = " ")
        count = count + 1
        red = red + 1
        if red > 6:
            red = 1
            print()

print(f"Ukupno je ispisano {count} brojeva.")