eggs = int(input("How many eggs do you have: "))
per_box = int(input("One box can have how many eggs: "))
boxes = eggs // per_box + (1 if eggs % per_box else 0)
for i in range(1, boxes + 1):
    if i < boxes:
        eggs_in_box = per_box
    else:
        eggs_in_box = eggs % per_box if eggs % per_box else per_box
    print("Box", i, ": [" + "o" * eggs_in_box + "]", sep="")
