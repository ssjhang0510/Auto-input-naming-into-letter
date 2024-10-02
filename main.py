# python already open this file and save to file for next manipulation
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    contents = file.write("\nNew text.")
