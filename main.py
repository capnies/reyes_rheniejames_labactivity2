#Develop a menu-driven Python program that stores 
#and processes structured student or product data using the required data types.

#The program must demonstrate create, read, update, 
#and display operations using strings, lists, tuples, and dictionaries.

#The program: Add student, see all students, delete student, and update student data.
#The student has an ID, name, program of school, and what year they are.

#needed functions ID, Name, Program of School, Year

#first, we put it in a tuple, after tuple then put it in list, then we use the ID as key list to
# dictionary if we ever need to find it. sounds easy.... right? Man I forgot how to do python
#dumbahh forgot how to convert string to int

#DISCLAIMER!!!!
#Some part of this code has been modified by AI. 
#Specifically, error input validation and printing of the students.
#The rest of the code, I did it.

#Final Code

def main():
    student_dictionary = {}
    student_list = []

    def getIntInput(prompt):
        while True:
            raw = input(prompt)
            try:
                return int(raw)
            except ValueError:
                print("That's not a valid number, please try again.\n")

#Madded an updater since my last work featured a certain function only update, which in turn has a fundamental flaw:
#It does not update.
    def updateDictionary():
        student_dictionary.clear()

        for student in student_list:
            student_dictionary[student[0]] = {
                "name": student[1],
                "program": student[2],
                "year": student[3]
            }

    def addStudent():
        idStudent = getIntInput("What is the ID: ")

        # Make sure we don't silently add a second student with an ID that's
        # already taken (the dictionary would just overwrite the old one).
        if idStudent in student_dictionary:
            print("A student with that ID already exists. Please use a different ID.\n")
            return

        nameStudent = str(input("What is the name: "))
        programStudent = str(input("What is the program: "))
        yearStudent = str(input("What grade year is the student: "))

        student = (idStudent, nameStudent, programStudent, yearStudent)

        student_list.append(student)
        updateDictionary()

        print("Student is successfully added! \n")

    def editStudents():

        #change into dictionary the student tuple list first
        #we could go to a nested dictionary
        updateDictionary()

        idS = getIntInput("Please type the ID of the student you want to change the information of: ")

        if idS not in student_dictionary:
            print("Student does not exist.\n")
            return

        print(f""" 
Student Number: {idS}
Name: {student_dictionary[idS]['name']}
Program: {student_dictionary[idS]['program']}
Year Level: {student_dictionary[idS]['year']} 
""")

        print("What information do you want to change?\n"
        "1. ID Number\n"
        "2. Name \n"
        "3. Program \n"
        "4. Year Level")

        op = getIntInput("Please enter here: ")

        # Find the student's position in the list
        studentIndex = None
        for i, student in enumerate(student_list):
            if student[0] == idS:
                studentIndex = i
                break

        # Defensive check: if list and dictionary ever fell out of sync,
        # don't crash further down trying to use a None index.
        if studentIndex is None:
            print("Student does not exist.\n")
            return

        oldStudent = student_list[studentIndex]

        match op:
            case 1:
                idNew = getIntInput("Please enter the new ID value: ")

                # Also guard against renaming a student into an ID that
                # another student already has.
                if idNew in student_dictionary and idNew != oldStudent[0]:
                    print("That ID is already taken by another student.\n")
                    return

                newStudent = (
                    idNew,
                    oldStudent[1],
                    oldStudent[2],
                    oldStudent[3]
                )

                print("Successfully Changed the ID! \n")

            case 2:
                nameNew = input("Please enter the new value for Name: ")

                newStudent = (
                    oldStudent[0],
                    nameNew,
                    oldStudent[2],
                    oldStudent[3]
                )

                print("Successfully Changed the Name! \n")

            case 3:
                programNew = input("Please enter the new value for Program: ")

                newStudent = (
                    oldStudent[0],
                    oldStudent[1],
                    programNew,
                    oldStudent[3]
                )

                print("Successfully Changed the Program! \n")

            case 4:
                YLNew = input("Please enter the new value for Year Level: ")

                newStudent = (
                    oldStudent[0],
                    oldStudent[1],
                    oldStudent[2],
                    YLNew
                )

                print("Successfully Changed the Year Level! \n")

            case _:
                print("Unknown input")
                return

        student_list[studentIndex] = newStudent
        updateDictionary()

    def deleteStudents():
        idS = getIntInput("Please type the ID of the student you want to delete: ")
        for i, student in enumerate(student_list):
            if student[0] == idS:
                studentIndex = i
                break
        else:
            print("Student does not exist.\n")
            return

        print(f"""
    Student Number: {student_list[studentIndex][0]}
    Name: {student_list[studentIndex][1]}
    Program: {student_list[studentIndex][2]}
    Year Level: {student_list[studentIndex][3]}
    """)

        confirm = input("Are you sure you want to delete this student? (Y/N): ")

        if confirm.upper() == "Y":
            student_list.pop(studentIndex)
            updateDictionary()
            print("Student successfully deleted!\n")
        else:
            print("Deletion cancelled.\n")


    def viewStudents():
        print("\n =====STUDENT LIST====")

        if not student_list:
            print("No students to show yet.\n")
            return

        # Column widths, based on header length vs longest value in each column,
        # so the table lines up even as names/programs get longer.
        idWidth = max(len("ID"), max(len(str(s[0])) for s in student_list))
        nameWidth = max(len("Name"), max(len(s[1]) for s in student_list))
        programWidth = max(len("Program"), max(len(s[2]) for s in student_list))
        yearWidth = max(len("Year"), max(len(s[3]) for s in student_list))

        header = (
            f"{'ID':<{idWidth}} | {'Name':<{nameWidth}} | "
            f"{'Program':<{programWidth}} | {'Year':<{yearWidth}}"
        )
        print(header)
        print("-" * len(header))

        for student in student_list:
            idS, nameS, programS, yearS = student
            print(
                f"{idS:<{idWidth}} | {nameS:<{nameWidth}} | "
                f"{programS:<{programWidth}} | {yearS:<{yearWidth}}"
            )

        print("\nSuccessfully Loaded all students! \n")


    while True:
        print("1. Add Student\n"
        "2. Edit Student\n"
        "3. Delete Student \n"
        "4. View All Students\n"
        "5. Exit\n")

        opt = getIntInput("Please enter the number: ")

        match opt:
            case 1:
                addStudent()
            case 2:
                editStudents()
            case 3:
                deleteStudents()
            case 4:
                viewStudents()
            case 5:
                break
            case _:
                print("Please choose a number from 1 to 5.\n")

if __name__ == "__main__":
    main()