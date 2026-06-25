marks1=int(input("Enter marks of first subject: "))
marks2=int(input("Enter marks of second subject: "))
marks3=int(input("Enter marks of third subject: "))

if(marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass in all subjects.")
else:
    print("You are not pass in all subjects.")

# Check for total percentage
total=marks1+marks2+marks3
percentage=total/3
print("Total marks:", total)
print("Percentage:", percentage)

if percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("You are pass.")
else:
    print("You are fail.")