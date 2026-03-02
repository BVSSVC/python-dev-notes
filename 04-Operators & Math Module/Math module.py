# %%
import math
print(math.floor(1.7))
print(math.floor(1.5))
print(math.floor(-1.5))
# %%
print(math.ceil(1.7))
print(math.ceil(1.5))
print(math.ceil(-1.5))
# %%
print(math.trunc(1.7))
print(math.trunc(1.2))
print(math.trunc(1.7234))
# %%
print(abs(2-10))
# %%
print(round(1.2))
print(round(1.5))
print(round(1.7))
print(round(2.5))
# %%
price=35.5478
print(round(price,2))
print(round(price,1))
# %%
help(round)
# %%
import random
print(random.random()) #between 0.0 and 1.0
# %%
print(random.randint(1,10))

# %%
x=7
y=7.1
print(x.is_integer())
print(y.is_integer())
# %%
x=7
y=7.1
print(isinstance(x,int))
print(isinstance(y,int))
# %%
# boolean function
email=""
address=''
name="Venkata Siva Sai Vardhan"
print(any([email,address,name]))
# %%
email=""
address=''
name="Venkata Siva Sai Vardhan"
print(all([email,address,name]))
# %%
#boolean functions
email=""
address=""
name=''
print(any([email,address,name]))
# %%
#boolean functions
email="saibabburi199@gmail.com"
address="8110 180th st w"
name='venkata siva sai vardhan'
print(all([email,address,name]))
# %%
