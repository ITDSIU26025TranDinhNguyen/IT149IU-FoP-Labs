def name_score(name):
    score = 0
    for c in name:
        score = score + ord(c)
    return score
n = int(input("How many names: "))
names = []
for i in range(n):
    name = input("Enter name: ")
    names.append(name)
highest_name = names[0]
highest_score = name_score(names[0])
for name in names:
    print(name, "score:", name_score(name))
    score = name_score(name)
    if score > highest_score:
        highest_score = score
        highest_name = name
print("Winner:", highest_name)
