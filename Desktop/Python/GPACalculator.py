#Students Number
students = int(input("Enter number of students: "))

#Students Names
names = [ ]
for i in range(students):
    name = input("Enter name of students: ")
    names.append(name)

#Students Results
maths = [ ]
physc = [ ]
scien = [ ]
coding = [ ]
eng = [ ]
for i in range(students):
    print("Result for the student ", names[i])
    math = float(input("Enter the mark of math for the student: "))
    physcs = float(input("Enter the mark of math for the student: "))
    sci = float(input("Enter the mark of math for the student: "))
    code = float(input("Enter the mark of math for the student: "))
    en = float(input("Enter the mark of math for the student: "))
    maths.append(math)
    physc.append(physcs)
    scien.append(sci)
    coding.append(code)
    eng.append(en)

#GPA Calculator
GPA = [ ]
for i in range(students):
    GPA1 = (maths[i] + physc[i] + scien[i] + coding[i] + eng[i]) / 5
    GPA.append(GPA1)

# the results
res = [ ]
for i in range(students):
    if GPA[i] >= 50:
        result = "pass"
    else:
        result = "Fail"
    res.append(result)
    print (names[i], GPA[i], res[i])