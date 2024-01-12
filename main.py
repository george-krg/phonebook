""" A script to provide write and read access to a contact book file """

names = []
phones = []

with open("contact.dat", "a+") as fr:
    # Read all the lines of the file into a list
    fr.seek(0, 0)
    lines = fr.readlines()


for line in lines:
    contact = line.split(":")
    names.append(contact[0])
    phones.append(contact[1])


print(lines)

state = 0

while state >= 0:
    if state == 0:
        sel = input(
            "If you want to search for a contact enter 1 - To add a new contact enter 2 - To exit enter q\n"
        )
        if sel == "1":
            state = 1
        elif sel == "2":
            state = 2
        elif sel == "q":
            state = -1
    elif state == 1:
        searchname = input(
            "Enter the name or part of the name to search for\n"
        )
        index = 0
        found = False
        for name in names:
            if searchname in name:
                print(name + ":" + phones[index])
                found = True
            index += 1
        if not found:
            print("There is no such entry\n")
        state = 0

    elif state == 2:
        name = input("Enter the name\n")
        number = input("Enter the number\n")
        sel = input(
            "To store the new contact press s - To go at the initial menu press b\n"
        )
        if sel == "s":
            with open("contact.dat", "a+") as f:
                f.write(name + ":" + number + "\n")
            names.append(name)
            phones.append(number)
            state = 0
        elif sel == "b":
            state = 0

if state == -1:
    print("Goodbye!\n")
