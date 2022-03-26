def main():
    lastName = input("Enter last name: ")
    firstName = input("Enter first name: ")
    studentID = input("Enter ID: ")

    inFile = open("studentInfo.txt", 'a')
    inFile.write("Name: " + firstName + " " + lastName)
    inFile.write("\nStudentID: " + studentID)
    inFile.write("\n")
    inFile.close()
    print("Done! Data is saved in file: studentInfo.txt")
main()