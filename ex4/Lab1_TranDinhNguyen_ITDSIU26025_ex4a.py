eggs=int(input("How many eggs do you have:"))
per_box=int(input(" One box can have how many egg:"))

boxes= eggs // per_box + (1 if eggs % per_box else 0)
last_box_fill = eggs % per_box if eggs % per_box else per_box
need_to_fill_last = per_box - (eggs % per_box) if eggs % per_box else 0

print("Total eggs:", eggs)
print("Boxes needed:", boxes)
print("Eggs in last box:", last_box_fill)
print("Eggs needed to fill last box:", need_to_fill_last)
