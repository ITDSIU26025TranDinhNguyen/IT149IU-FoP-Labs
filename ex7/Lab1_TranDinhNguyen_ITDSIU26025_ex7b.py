base = 200
hours = [0, 5, 10, 15,20,25,30,35,40]

print(f'{"Hour":>5}\t{"Number of Bacteria":>8}')
for h in hours:
    B = base * (2 ** h)
    print(f'{h:>5}\t{B:>18}')
