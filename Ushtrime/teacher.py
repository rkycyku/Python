fillimi = input("A deshironi te filloni (Y/N): ")
fillimi = fillimi.upper()


while fillimi == "Y":
    studentname = input("\nEnter student name: ")
    while studentname == "":
        studentname = input("\nCannot leave field blank. Enter Again: ")   
    
    enterscore = int(input("How many scores: "))

    sslista = []

    for enterscore in range(enterscore):
        
        studentscore = int(input("\nEnter student score (0-100): "))
        sslista.append(studentscore)
        while studentscore <= -1 or studentscore >= 101:
            studentscore = int(input("\nInvalid score. Enter score again (0-100): "))
            sslista.append(studentscore)
    print(studentname,sslista)
    break