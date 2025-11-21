# Program to write names into a file

filename = "names.txt"
n = int(input("How many names do you want to enter? "))

with open(filename, "w") as f:
    for i in range(n):
        name = input(f"Enter name {i + 1}: ")
        f.write(name + "\n")

print("Names saved in", filename)
