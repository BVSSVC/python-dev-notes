# stand alone if
a=int(input("Enter a number: "))
print(f"The value of a is {a}")
if a>5:
    print("A is greater than 5")
print("End of flow")

#If – else statement (Two way-desicion else)
a=int(input("Enter a number: "))
print(f"The value of a is {a}")
if a%2==0:
    print("A is even")
else:
    print("A is odd")

# Greater between two numbers
a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))
print(f"The values of a and b are {a},{b}")
if a==b:
    print(f"Both a:{a} & b:{b} are equal ")
elif a>b:
    print(f"A:{a} is greater than B:{b} ")
else:
    print(f"A:{a} is less than B:{b} ")

#password
password=input("Enter your password.")
if password=="Bvss@8110":
    print("Login Successful")
else:
    print("Reattempt")


a=int(input("Enter your number: "))
print(f"The value of a is {a}")
if a%2==0:
    if a>10:
        print(f"A:{a} is even and greater than 10 ")
    elif a<10:
        print(f"A:{a} is even but less than 10 ")
    else:
        print(f"A:{a} is even and equal to 10")
else:
    print("A:{a} is odd number and no need to compare with 10.")

a=int(input("Enter a number for a: "))
b=int(input("Enter a number for b: "))
print(f"The value of a:{a} and b:{b}")
if a>=b:
    if a==b:
        print(f"Both A{a} and B:{b} are equal")
    else:
        print(f"A:{a} is greater than B:{b}")
else:
    print(f"A:{a} is less than B:{b}")


score=90
submitted_report=True
if score>=90:
    print("High Score")
else:
    print("Low Score")
if submitted_report:
    print("Project is submitted")
else:
    print("Project is not submitted")



email=" bsaivardhan7@gmail.com"
email=email.strip()
print(f"the email is {email}")
if email=="":
    print("Email cannot be empty")
elif not('.' in email and '@' in email):
    print("email must contain '.' and '@'")
elif email.count("@")!=1:
    print("Email must ccontain exactly one @")
elif not email.endswith((".com",".org",".net")):
    print("email must end with .com or .org or .net")
elif len(email)>254:
    print("Email must not be more than 254 characters")
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("email is valid")


email=" -bsaivardhan@7@gmail.com"
email=email.strip()
print(f"the email is {email}")
if email=="":
    print("Email cannot be empty")
if not('.' in email and '@' in email):
    print("email must contain '.' and '@'")
if email.count("@")!=1:
    print("Email must ccontain exactly one @")
if not email.endswith((".com",".org",".net")):
    print("email must end with .com or .org or .net")
if len(email)>254:
    print("Email must not be more than 254 characters")
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("email is valid")

email="bsaivardhan7@gmail.com"
valid=True
email=email.strip()
print(f"the email is {email}")
if email=="":
    print("Email cannot be empty")
    valid=False
if not('.' in email and '@' in email):
    print("email must contain '.' and '@'")
    valid=False
if email.count("@")!=1:
    print("Email must ccontain exactly one @")
    valid=False
if not email.endswith((".com",".org",".net")):
    print("email must end with .com or .org or .net")
    valid=False
if len(email)>254:
    print("Email must not be more than 254 characters")
    valid=False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid=False
if valid:
    print("email is valid")