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
def winner(names_list):
    highest_name = names_list[0]
    highest_score = name_score(names_list[0])
    for name in names_list:
        score = name_score(name)
        if score > highest_score:
            highest_score = score
            highest_name = name
    return highest_name

for name in names:
    print(name, "score:", name_score(name))
print("Winner:", winner(names))
