students = {}

while True:
    print("\nA:Add  B:Update  C:Search  D:Display  E:Exit")
    ch = input("Enter choice: ")

    if ch == 'A':
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks

    elif ch == 'B':
        name = input("Name to update: ")
        if name in students:
            students[name] = int(input("New marks: "))
        else:
            print("Not found")

    elif ch == 'C':
        name = input("Name to search: ")
        if name in students:
            print(students[name])
        else:
            print("Not found")

    elif ch == 'D':
        print(students)

    elif ch == 'E':
        break

    else:
        print("Wrong choice")