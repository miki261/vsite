n = int(input("Unesi realan broj: "))

if n%2 == 0:
    znak = "x"

else:
    znak = "*"

for i in range(1, n+1):
    print(znak*i)