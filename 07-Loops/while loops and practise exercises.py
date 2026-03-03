# %%
i=1
while i<=5:
    print(i)
    i+=1
# %%
c=0
n=180
while n>10:
    n=n/3
    c+=1
print(c)
# %%
a=int(input("Enter a number"))
while a<100 or a>500:
    print("Please enter number once again")
    a=int(input("Enter number between 100 and 500"))
else:
    print(f"The given number {a} is between 100 and 500")

# %%
a=10
while a>0:
    if a%2==0:
        print(f"even number:{a}")
    else:
        print(f"odd number:{a}")
    a-=1
# %%
name="saivardhan2624"
l=len(name)
b=0
while b<l:
    if name[b].isdecimal():
        break
    else:
        print(name[b])
    b+=1
# %%
name="saivardhan2624"
l=len(name)
b=0
while b<l:
    if not name[b].isalpha():
        continue
    print(name[b])
    b+=1
# %%
n=0
while n<=5:
    j=0
    while j < n:
        print("*",end=" ")
        j+=1
    print()
    n+=1
# %%
i=1
while i<5:
    print(i)
    i+=1
else:
    print("loop executed succesfully")
# %%
i=1
while i<5:
    if i>2:
        break
    print(i)
    i+=1
else:
    print("loop executed succesfully")
# %%
i=10
while i>0:
    print(i)
    i-=1
# %%
n=1
while n<=10:
    print(n)
    n+=1
# %%
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# %%
n=756
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
print(sum)
# %%
a=4
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")
# %%
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>500:
        break
    elif num>150:
        continue
    elif num%5==0:
        print(num)
# %%
n=756
count=0
while n>0:
    n=n//10
    count+=1
print(count)
# %%
for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()
# %%
list1 = [10, 20, 30, 40, 50]
for item in list1[::-1]:
    print(item)
# %%
list1 = [10, 20, 30, 40, 50]
a=len(list1)
while a>0:
    print(list1[a-1])
    a-=1
# %%
start=10
stop=25
for i in range(start,stop+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
# %%
n=10
a=0
b=1
while n>0:
    print(a,end=",")
    temp=a+b
    a=b
    b=temp
    n-=1
# %%
n=10
a=0
b=1
for i in range(n):
    print(a,end=",")
    a,b=b,a+b
print()
# %%
n=5
sum=1
for i in range(n,0,-1):
    sum=sum*i
print(sum)
# %%
a=75642
n=0
while a>0:
    r=a%10
    a=a//10
    n=(n*10)+r
print(n)
# %%
a=str(1052)
smallest=int(a[0])
largest=int(a[0])
for i in a:
    digit_int=int(i)
    if digit_int>largest:
        largest=digit_int
    if digit_int<smallest:
        smallest=digit_int
print("Smallest:", smallest)
print("Largest:", largest)

# %%
