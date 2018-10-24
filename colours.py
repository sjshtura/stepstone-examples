colours = ["red"]
colours_copy = colours
for i in colours_copy:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)