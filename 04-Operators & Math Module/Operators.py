# %%
# Arithmetic operators
a=10
b=5
print("The sum of {},{} is {}".format(a,b,a+b))
print("The difference of {},{} is {}".format(a,b,a-b))
print("The division of {},{} is {}".format(a,b,a/b))
print("The multiplcation of {},{} is {}".format(a,b,a*b))
print("The modulus of {},{} is {}".format(a,b,a%b))
print("The floor division of {},{} is {}".format(a,b,a//b))
# %%
# Comparision operators
a=10
b=3
print("a>b :",a>b)
print("a<b :",a<b)
print("a>=b :",a>=b)
print("a<=b :",a<=b)
print("a==b :",a==b)
print("a!=b :",a!=b)
# %%
print((3<2) and (3>2))
print((3>2) and (5<6))
print((3<2) or (3>2))
print((3<2) or (5>2))
print(not((3<2) and (3>2)))
# %%
print("\nAssignment Operators")
c=5
print(f"The initial value of c is {c}")
c+=2
print(f"The value of c after c+= is {c}")
c-=2
print(f"The value of c after c-= is {c}")
c*=2
print(f"The value of c after c*= is {c}")
c/=2
print(f"The value of c after c/= is {c}")
c**=2
print(f"The value of c after c**= is {c}")
c//=2
print(f"The value of c after c//= is {c}")
# %%
# membership operators
a='sai'
print("a" in a)
print("z" in a)
print("z" not in a)
# %%
a=[1,'sai',True,10.5,None]
b='saivardhan'
print(a[1] in b)
print(a[1] not in b)
# %%
a=5
b=5
print(a is b)
print(a is not b)
# %%
