
a = int(input("Vvedite kolichesvo elementov:"))
b = []

for i in range(0, a):
    elem = int(input("Vvedite element"))
    b.append(elem)
avg = sum(b) / a
print("srednee chislo:", avg)
