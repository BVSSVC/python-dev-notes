# %%
for i in (1,2,3,4,5):
    print(f"Round:{i}")
# %%
items=(1,2,3,4,5)
for i in items:
    print(f"Round:{i}")
# %%
items=[1,2,3,4,5,"hello"]
for i in items:
    print(f"Round:{i}")
# %%
items="hello"
for i in items:
    print(f"Round:{i}")
# %%
for i in range(5):
    print(f"Round : {i}")
# %%
for i in range(1,5):
    print(f"Number: {i}")
# %%
for i in range(0,10,2):
    print(f"Number: {i}")
# %%
for i in range(15,5,-1):
    print(f"Number:{i}")
# %%
num=[100,200,300,400,500,600]
sum=0
n=0
for i in num:
    sum+=i
    n+=1
avg=sum/n
print(f"The average of {num} is {avg}")
# %%
for i in range(1,11):
    if i%2==0:
        print(f"{i}:Even Number")
    else:
        print(f"{i}:Odd Number")
# %%
numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers:
    if i>15:
        break
    else:
        print(i)
# %%
names=['maria','john','','kumar']
for name in names:
    if name=='':
        print("Empty name detected")
        break
    else:
        print(f"Name:{name}")
# %%
name='Venkata Siva Sai Vardhan Babburi'
count=0
for char in name:
    if char!='a':
        continue
    else:
        count=count+1
print(f"The alphabet A has occurred in the {name}:{count} times.")
# %%
names=['maria','john','','kumar']
for name in names:
    if name=='':
        name=name.replace('',"Unknown Name")
    print(f"Name:{name}")
# %%
days=['Mon','Tue','Wed','Thu','Fri','Sat']
weekdays=['Sat','Sun']
for day in days:
    if day in weekdays:
        continue
    else:
        print(f"The working days are {day}")
# %%
for i in range(1,6):
    print(f"The number is {i}")
else:
    print("Loop completed")
# %%
count=0
for i in range(1,6):
    count=count+1
    if count>2:
        break
    else:
        print(f"The number is {i}")
else:
    print("Loop completed")
# %%
for i in range(5,-1,-1):
    print(f"Number:{i}")
# %%
num=[1,2,3,4,5,6,7,8,9]
for i in reversed(num):
    print(i)
# %%
bun=5
for i in range(bun,-1,-1):
    print(f"Number:{i}")
# %%
num=[1,2,3,4]
for i in num[::-1]:
    print(i)

# %%
for i in range(0,3):
    for j in range(0,2):
        print(f"({i},{j})")
# %%
for i in range(0,3):
    for j in range(0,2):
        for z in range(2):   
            print(f"({i},{j},{z})")
# %%
colors=['red','green','blue']
sizes=['L','M','S']
for color in colors:
    for size in sizes:
        print(f"{color}-{size}")
    print()
# %%
years=[2026,2027]
months=['Jan','Feb']
days=[1,2,3]
for year in years:
    for month in months:
        for day in days:
            print(f"{year}_{month}_{day}.csv")
# %%
tables=["order",'customers','products']
columns=['id','create_date']
for table in tables:
    for column in columns:
        print(f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL")
# %%
