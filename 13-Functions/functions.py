# %%
def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add milk")
    print("Enjoy it!")
print("Wake up")
make_coffee()
print("Working for a while")
make_coffee()
make_coffee()
# %%
import math
print(len("Python"))
# Function from libraries
number = 4.2
print(math.ceil(number))
# %%
def clean_name(name):
    print(name.strip().lower())
clean_name("MariA  ")
clean_name("KUMAR ")
clean_name()
# %%
case_rule = 'lower'
def clean_name(name):
    cleaned = name.strip()
    if case_rule=='lower':
        cleaned = cleaned.lower()
        print("Raw:", name)
        print('cleaned:', cleaned)
clean_name("MariA  ")
clean_name("KUMAR ")
print(f"The Rule is:{case_rule}")
# %%
def caluclator(a,b):
    add = a+b
    return add
res = caluclator(20,5)
print("Addition:", res)
# %%
def caluclator(a,b):
    add = a+b
    print(add)
res = caluclator(20,5)
print("Addition:", res)
# %%
def is_even(list1):
    even_num = []
    for item in list1:
        if item %2 ==0:
            even_num.append(item)
    return even_num
even_num = is_even([2, 3, 42, 51, 62, 70, 5, 9])
print("Even numbers are:", even_num)
# %%
def arithmetic(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    division = num1/num2
    return add, sub, division
res = arithmetic(10,2)
a,b,c = res
print(res,type(res))
print("Addition: ", a)
print("Subtraction: ", b)
print("Division: ", c)
# %%
def addition(num1, num2):
    # Implementation of addition function in comming release
    # Pass statement 
    pass

addition(10, 2)
# %%
global_lang = 'english'
def var_scope():
    local_lang = 'Python'
    print(local_lang)
var_scope()
print(global_lang)
print(local_lang)
# %%
def function1():
    # local variable
    loc_var = 888
    print("Value is :", loc_var)

def function2():

    print("Value is :", loc_var)

function1()
function2()
# %%
glo_var = 999
def function1():
    # local variable
    print("Value is :", glo_var)

def function2():

    print("Value is :", glo_var)
function1()
function2()
# %%
glo_var = 999
def function1():
    # local variable
    print("Value is :", glo_var)

def function2():
    glo_var = 5432
    print("Value is :", glo_var)
def function3():
    print("Value in 3rd function :", glo_var)
function1()
function2()
function3()
# %%
glo_var = 999
def function1():
    # local variable
    print("Value is :", glo_var)

def function2():
    global glo_var
    glo_var = 5432
    print("Value is :", glo_var)
def function3():
    print("Value in 3rd function :", glo_var)
function1()
function2()
function3()
# %%
def outer_func():
    x = 777
    def inner_func():
        nonlocal x
        x = 700
        print("Value of x inside inner function is :",x)
    inner_func()
    print("value of x inside outer function is :", x)
outer_func() 
# %%
def clean_name(first_name,last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    full_name = first_name + ' ' + last_name
    print(full_name)
clean_name("MariA  ","    BaBBuri")
# %%
def clean_name(first_name,last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    full_name = first_name + ' ' + last_name
    print(full_name)
clean_name("BabbUri Sai  ","    MaRia")
# %%4
def clean_name(first_name,last_name,country):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    full_name = first_name + ' ' + last_name
    print(full_name,"From",country)
clean_name("BabbUri Sai  ","    MaRia","INDIA")
clean_name(first_name='sai BabbURI',country="USA",last_name="BABBURI")
# %%
# function with default argument
def message(name="Guest"):
    print("Hello", name)

# calling function with argument
message("John")

# calling function without argument
message()
# %%
# %%4
def clean_name(first_name,last_name,country='n/a'):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    full_name = first_name + ' ' + last_name
    print(full_name,"From",country)
clean_name("BabbUri Sai  ","    MaRia","INDIA")
clean_name(first_name='sai BabbURI',last_name="BABBURI")
# %%
def total(*args):
    print(sum(args))
total(1,2,3,4,5)
# %%
def addition(*numbers):
    sum = 0
    for no in numbers:
        sum = sum + no
    print("Sum is:", sum)
addition()
addition(10,20,30,40,50)
addition(67,45.4,65)
# %%
def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)
create_user(first_name='Mo',
            last_name='sai',
            age=33,
            country='egypt')
# %%
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of a number is:",factorial(8))
# %%
l = [10,20,30,40,50,60,11,222,333]
even_nos = list(filter(lambda x:x%2==0,l))
print(even_nos)
# %%
l = [10,20,30,40,50,60,11,222,333]
cube_nos = list(map(lambda x:x**3,l))
print(cube_nos)
# %%
from functools import reduce
l = [10,12,13,4,8,9]
add = reduce(lambda x,y:x+y,l)
print(add)
# %%
def write_log(message):
    with open(r"C:\users\bsaiv\Documents\app.log","a") as file:
        file.write(message+"\n")
write_log("App started")
write_log("Users created")   
# %%
def clean_email(email):
    cl_email = email.strip().lower()
    username,domain = cl_email.split("@")
    return {"username":username,
            "domain":domain}
print(clean_email("saibabburi1999@gmail.com"))
# %%
def is_valid_password(password):
    return len(password)>=8
print(is_valid_password("123456"))
print(is_valid_password("12345678"))
# %%
def is_valid_email(email):
    return "@" in email and "." in email
print(is_valid_email("saibabburi1999@gmail.com"))
print(is_valid_email("saibabburi1999@gmailcom"))

# %%
write_log("App Started")
email = input("Enter an email id")
if not is_valid_email(email):
    write_log(f"Invalid email received:{email}")
else:
    clean=clean_email(email)
    write_log(f"processed email:{clean}")
write_log("App ended")
# %%
