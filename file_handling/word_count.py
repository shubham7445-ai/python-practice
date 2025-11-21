# Program to count words in a text file

filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        text = f.read()
        words = text.split()
        print("Number of words in the file:", len(words))
except FileNotFoundError:
    print("File not found.")
