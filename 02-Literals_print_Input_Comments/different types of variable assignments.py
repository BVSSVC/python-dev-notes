x=10 # single assignment (Called hardcoding(static assignemnt))
# Multiple Variable assignemnts
a,b,c=10,20,30
print(x)
print(a)
print(b)
print(c)

# %%
# same value to multiple variable assignment
a=b=c=10
print(a,b,c)
#id() is one of Python’s simplest but most revealing built‑in functions. 
#It tells you the identity of an object — essentially where that object lives in memory.
print(id(a))
print(id(b))
print(id(c))

# %%
a,b,c=[10,"sai",True]
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
# %%
# swapping values without any temporary variable
a,b=10,20
print("Value of a is :",a)
print("Value of b is :",b)
a,b=b,a
print("After SwappingValue of a is :",a)
print("After Swapping Value of b is :",b)

# %%
a,*b=[10,20,20,40]
print("Value of a is :",a)
print("Value of b is :",b)
# %%
*a,b=[10,20,20,40]
print("Value of a is :",a)
print("Value of b is :",b)
# %%
x=10
print(x)
del x
print(x)
# %%
