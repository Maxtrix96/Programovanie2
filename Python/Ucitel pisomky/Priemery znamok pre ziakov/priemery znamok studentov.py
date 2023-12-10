import os

filePath = os.path.abspath(__file__)
relativeTextFilePath1 = os.path.join("..", "student grade log.txt")
textFilePath1 = os.path.abspath(os.path.join(filePath, relativeTextFilePath1))
relativeTextFilePath2 = os.path.join("..", "student grade average.txt")
textFilePath2 = os.path.abspath(os.path.join(filePath, relativeTextFilePath2))

def edit_student_file(StudentFile):
    overallAverage = 0
    allGrades = []
    subjectAverage = 0
    subjectGradesList = StudentFile[1:]
    updatedStudentFile = [StudentFile[0]]

    for item in subjectGradesList:
        SubjGrades = [int(num) for num in item.split(":")[1].split(",")]
        subjectAverage = round(sum(SubjGrades) / len(SubjGrades), 2)
        subjectReport = f"{item} Priemer: {subjectAverage}"
        updatedStudentFile.append(subjectReport)
        allGrades.append(SubjGrades)
    
    overallGrades = []
    for item in allGrades:
        overallGrades += item

    overallAverage = round(sum(overallGrades) / len(overallGrades), 2)
    updatedStudentFile[0] += f"Celkovy priemer: {overallAverage}"
    
    return updatedStudentFile

with open(textFilePath1, "r", encoding="utf-8") as file:
    gradeLog = file.read().split("\n ")
    splitGradeLog = []
    for item in gradeLog:
        studentInfo = item.split("\n")
        splitGradeLog.append(studentInfo[1:])
    
    updatedGradeLog = []
    for student in splitGradeLog:
        updatedGradeLog.append(edit_student_file(student))
    
    finalGradeLog = []
    for item in updatedGradeLog:
        finalGradeLog += ["\n "] + item 

with open(textFilePath2, "w", encoding="utf-8") as file:
    file.write("\n".join(finalGradeLog).replace("\n\n", "\n")[1:]) 