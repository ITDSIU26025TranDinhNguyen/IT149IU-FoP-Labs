base = 200
hours = int(input("Max hours:"))
print("Hour\tNumber of Bacteria")
for h in range (0,hours + 1):
    B  = base * (2 ** h)
    print(f"{h}\t{B}")
