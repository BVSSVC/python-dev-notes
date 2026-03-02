# %%
# Implict conversion
a=100
b=456.7
c=a+b
print(f"The value of a is {a} and type of a is {type(a)}")
print(f"The value of a is {b} and type of a is {type(b)}")
print(f"The value of a is {c} and type of a is {type(c)}")
# %%
salary='10000'
tax_amount="1000"
net_income=salary-tax_amount
print("Net income is:",net_income)
# %%
# In such cases we would want to convert the type of variable
# str to int() conversion
salary='10000'
tax_amount="1000"
net_income=int(salary)-int(tax_amount)
print("Net income is:",net_income)
# %%
# int()
# 1. We can convert from any type to int except complex type.
print(int(10.56))
print(int("100"))
print(int(True))
print(int(False))
# %%
print(int('10.56'))
# %%
#float()
#1. We can convert any type value to float type except complex type. 
#2. Whenever we are trying to convert str type to float type compulsary str should be either integral or floating point literal and should be specified only in base-10.    
print(float(10))
print(float("10.567"))
print(float("100"))
print(float(True))
print(float(False))
# %%
print(float(10+5j))
# %%
#bool()
print(bool(1))
print(bool(0))
print(bool(10))
print(bool(10.56))
print(bool(""))
print(bool(" "))
print(bool("sai"))
print(bool(10+5j))
print(bool(0+0j))
# %%
#str()
print(str(10))
print(str(True))
print(str(10+5j))
print(str(10.56))
# %%
