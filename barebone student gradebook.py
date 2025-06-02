studentArray = []

def start():
    whatDo = input("1. Add Student | 2. Add Subject Grade | 3. Review Student Grade | 4. View Class Average | 5. Exit" + 
                    "\nWhat do you wish to do? ")
    next = checkValid(whatDo)
    nextOperation(next)
    
def checkValid(whatDo):
    if whatDo.isnumeric():
        whatDo = int(whatDo)
        return whatDo
    else:
        print("Enter a valid option")
        return -1

def nextOperation(whatDo):
    if whatDo == -1:
        return start()
    match whatDo:
        case 1:
            addStudent()
        case 2:
            addSubGrade()
        case 3:
            viewStudentGrade()
        case 4:
            studentAvg()
        

def addStudent():
    name = input("What is the student's full name? ")
    addGrade = input(f"Do you wish to add a subject and grade in {name}'s gradebook? (y/n) ").lower()
    if addGrade == "y":
        subjectName = input("What subject do you wish to add? ")
        while True:
            grade = input(f"{subjectName}'s grade?")
            if grade.isnumeric():
                grade = int(grade)
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade should be 0 - 100")
            else:
                print("Enter a valid value")
        newDict = {
            "name" : name,
            subjectName : grade
        }
        studentArray.append(newDict)
    else:
        newDict = {
            "name" : name
        }
        studentArray.append(newDict)

def addSubGrade():
    found = False
    name = input("What is the full name of the student? ")
    for student in studentArray:
        if student["name"] == name:
            subjectName = input("What subject do you wish to add? ")
            while True:
                grade = input(f"{subjectName}'s grade?")
                if grade.isnumeric():
                    grade = int(grade)
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade should be 0 - 100")
                else:
                    print("Enter a valid value")
            student.update({subjectName: grade})
            found = True
            break
    if not found:
        print("Student does not exist.")
        

def viewStudentGrade():
    found = False
    name = input("What is the name of the student you wish to view? ")
    for student in studentArray:
        if student["name"] == name:
            for key, value in student.items():
                print(key, value)
            found = True
            break
    if not found:
        print("Student does not exist.")

def studentAvg():
    studentGrades = []
    total = 0
    noOfSubs = 0

    for student in studentArray:
        for values in student.values():
            if isinstance(values, str):
                continue
            else:
                studentGrades.append(values)
                noOfSubs += 1
    
    for x in studentGrades:
        total += x

    avg = total / noOfSubs
    return avg

start()