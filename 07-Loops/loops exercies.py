# %%
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=",")
    print()
# %%
for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
# %%
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
# %%
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end=" ")
    print()
# %%
c=5
for i in range(5):
    for j in range(5,i,-1):
        print(c,end=" ")
    print()
# %%
for i in range(5):
    for j in range(5,i,-1):
        print(j,end=' ')
    print()
# %%
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
# %%
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()
# %%
rows=6
for i in range(1,rows):
    print(" "*(5-i),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
# %%
for i in range(1,6):
    for j in range(1,6):
        if j>i:
            print(j,end=' ')
        else:
            print(i,end=" ")
    print()
# %%
for i in range(1,6):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()

# %%
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
# %%
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
# %%
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

# %%
for i in range(5):
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()

# %%
for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,5):
        print("*",end=" ")
    print()
# %%
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()
# %%
for i in range(4):
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,5):
        print("*",end=" ")
    print()

# %%
for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
# %%
for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(5,i,-1):
        print("*",end=" ")
    for j in range(5,i+1,-1):
        print("*",end=" ")
    print()
# %%
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
# %%
n=5
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
    n-=1
    print()
# %%
# %%
p=0
for i in range(1,6):
    for j in range(i):
        print(p,end=" ")
    p+=2
    print()
# %%
n=5

for i in range(n):
    for j in range(i+1):
       if i%2==0:
            print(1,end=" ")
       else:
           print(2,end=" ")
    print()
# %%
