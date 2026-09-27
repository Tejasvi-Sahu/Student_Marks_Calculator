# Student Marks Calculator

print("================================")
print("     STUDENT MARKS CALCULATOR")
print("================================")

name = input("Enter student name: ")

print("\nEnter marks out of 100")

maths = float(input("Maths: "))
python = float(input("Python: "))
dsa = float(input("DSA: "))
english = float(input("English: "))
coa = float(input("COA: "))

total = maths + python + dsa + english + coa
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n================================")
print("           RESULT")
print("================================")

print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

if percentage >= 40:
    print("Status       : PASS")
else:
    print("Status       : FAIL")

print("================================")