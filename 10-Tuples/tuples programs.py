# %%
my_tuple = (10,20,30)
print(my_tuple) #ordered

# %%
my_tuple = (10,20,30,10)
print(my_tuple) #ordered
# %%
my_tuple = (10,20,30)
print(my_tuple[0]) #ordered
# %%
my_tuple[3] = 40
print(my_tuple)
# %%
# string tuple
string_tuple = ('Jessa','emma','Kelly')
print(string_tuple)

# %%
# mixed type tuple
sample_tuple = (100,True,'sai vardhan',[1,True,'sai'])
print(sample_tuple)
# %%
single_tuple = ('Hello')
print(type(single_tuple))
# %%
single_tuple = ('Hello',)
print(type(single_tuple))
# %%
tuple1 = 1,2,'Hello'
print(tuple1)
print(type(tuple1))
# %%
i,j,k=tuple1
print(i,j,k)
# %%
tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
print(len(tuple1))
# %%
# create a tuple
sample_tuple = (1, 2, 3, "Hello", [4, 8, 16])
# iterate a tuple
for item in sample_tuple:
    print(item)
# %%
tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple1[1])
print(tuple1[-1])
print(tuple1[0])
# %%
print(tuple1[1:4])
print(tuple1[:4])
print(tuple1[::-1])
# %%
tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple1.index('T'))
# %%
tuple1 = (10, 20,60, 30, 40, 50, 60, 70, 80)
# Limit the search locations using start and end
# search only from location 4 to 6
# start = 4 and end = 6
# get index of item 60
print(tuple1.index(60))
print(tuple1.index(60,4,7))
# %%
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# checking whether item 50 exists in tuple
print( 50 in tuple1)
print(500 in tuple1)
# %%
tuple1 = (0, 1, 2, 3, 4, 5)
sample_list = list(tuple1)
sample_list.append(6)
tuple1=tuple(sample_list)
print(tuple1)
# %%
tuple1 = (10, 20, [25, 75, 85])
# before update
print(tuple1)
tuple1[2][0] = 255
print(tuple1)
# %%
tuple1 = (0, 1, 2, 3, 4, 5)
sample = list(tuple1)
sample[1]=10
tuple1 = list(sample)
print(tuple1)
# %%
tuple1 = (0, 1, 2, 3, 4, 5)
del tuple1
print(tuple1)
# %%
import itertools
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3=(item for item in itertools.chain(tuple1,tuple2))
print(tuple(tuple3))

# %%
nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")

# access the first item of the third tuple
print(nested_tuple[2][0])  # P

# iterate a nested tuple
for i in nested_tuple:
    print("tuple", i, "elements")
    for j in i:
        print(j, end=", ")
    print("\n")
# %%
