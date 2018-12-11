from datetime import datetime

print("1 for harry , 2 for rohan , 3 for nikhil")

person_select = int(input("choose person:"))

# Harry code
if (person_select == 1):
    add_see = int(input("1 for see the harry log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("harryexercise.txt","r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("harryexercise.txt","a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("harrydiet.txt","r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("harrydiet.txt","a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("harryexercise.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("harrydiet.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()


# Rohan code
if (person_select == 2):
    add_see = int(input("1 for see the rohan log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("rohanexercise.txt","r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("rohanexercise.txt","a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("rohandiet.txt","r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("rohandiet.txt","a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("rohanexercise.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("rohandiet.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

# Nikhil code
if (person_select == 3):
    add_see = int(input("1 for see the Nikhil log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("nikhilexercise.txt","r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("nikhilexercise.txt","a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("nikhildiet.txt","r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("nikhildiet.txt","a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("nikhilexercise.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("nikhildiet.txt","a")
            content = input("Write the log:")
            contentinfile = "\n"+str(datetime.now()) +" "+content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

