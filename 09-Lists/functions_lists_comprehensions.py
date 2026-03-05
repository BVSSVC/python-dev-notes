# %%
letters = ['a','b','c','d']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)
print(new_list)
# %%
letters = ['a','b','c','d']
print(enumerate(letters))
# %%
letters = ['a','b','c','d']
print(list(enumerate(letters)))
# %%
letters = ['a','b','c','d']
print(list(enumerate(letters,start=1)))
# %%
letters = ['a','b','c','d']
for index,value in enumerate(letters):
    print(index,value)
# %%
for i in zip(letters,letters):
    print(i)
# %%
for i in reversed(letters):
    print(i)
# %%
letters = ['a','b','c']
print(map(str.upper,letters))
# %%
letters = ['a','b','c']
print(list(map(str.upper,letters)))
# %%
numbers = ['1','2','3']
print(list(map(int,numbers)))
# %%
names = ['sai  ','   Babburi','   Vardhan  ']
for i in map(str.strip,names):
    print(i)
# %%
letters = ['a','b','c',"123"]
print(list(filter(str.isalpha,letters)))
# %%
letters = ['a','b','c',"123",None,False,True]
print(list(filter(None,letters)))
# %%
letters = ['a','b','c',"123",None,False,True]
print(list(filter(bool,letters)))
# %%
result = lambda x:x*2
print(result(10))
# %%
result = lambda x,y:x+y
print(result(10,20))
# %%
check  =lambda i: i in "python"
print(check('n'))
# %%
prices = ['$12.00','$9.45','$10.456']
result = list(map(lambda p:float(p.replace('$','')),prices))
print(result)
# %%
prices = [100,200,10,20,23,400,500]
result = list(filter(lambda p:p>=100,prices))
print(result)
# %%
prices = [['sai',100],['vardhan',200],['babburi',10]]
result = list(filter(lambda p:p[1]>=100,prices))
print(result)
# %%
domain = ['www.google.com',
          'openai.com',
          'localhost',
          'www.ml.com']
cleaned = [item.upper() for item in domain if item.endswith('.com')]
print(cleaned)
# %%
