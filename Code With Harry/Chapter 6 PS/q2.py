# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter subject 1 marks: "))
s2 = int(input("Enter subject 2 marks: "))
s3 = int(input("Enter subject 3 marks: "))

avg = (s1+s2+s3)/3

if(s1 >33 and s2>33 and s3>33 and avg >40):
    print("Student pass")
else:
    print("Student fails")