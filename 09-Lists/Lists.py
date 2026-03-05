# %%
# creating lists
empty = []
letters=['a','b','c','d']
numbers=[1,2,3]
mixed_list=[1,3.14,10+5j,'sai',True,None]
print(empty,type(empty))
print(letters,type(letters))
print(numbers,type(numbers))
print(mixed_list,type(mixed_list))
# %%
# using list()
empty = list()
print(empty,type(empty))
letters=list('python')
print(letters,type(letters))
numbers=list(range(5))
print(numbers,type(numbers))
# %%
matrix=[['a','b','c'],
        ['d','e','f']]
print(matrix,type(matrix))
mixed_matrix=[['a','b','c'],
        [1,'sai',True],
        ["Venkata Babburi"]]
print(mixed_matrix,type(mixed_matrix))
# %%
# Access & Read
# Indexing to access specific element
lst = ['a','b','c','d']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])
print()
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
print(matrix[2])
print(matrix[-1])
print(matrix[-1][2])
print(matrix[-1][-1])
print(matrix[0][0])
print()
# slicing to get few elements
lst=['a','b','c','d']
print(lst[0:3])
print(lst[2:])
print(lst[:])
print(lst[:2])
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
print(matrix[0:2])
print(matrix[1:])
print(matrix[2][:2])
# %%
# unpacking lists
person = ['sai vardhan',29,'data engineer','spain']
name,age,role,country = person
print(name,type(name))
print(role,type(role))
# %%
person = ['sai vardhan',29,'data engineer','spain']
name,*details,country = person
print(name,type(name))
print(details,type(details))
print(country,type(country))
# %%
person = ['sai vardhan',29,'data engineer','spain']
name,*details = person
print(name,type(name))
print(details,type(details))

# %%
person = ['sai vardhan',29,'data engineer','spain']
*details,country = person
print(details,type(details))
print(country,type(country))
# %%
person = ['sai vardhan',29,'data engineer','spain']
name,_,_,country = person
print(name,type(name))
print(country,type(country))
# %%
person = ['sai vardhan',29,'data engineer','spain']
name,*_,country = person
print(name,type(name))
print(country,type(country))
# %%
numbers = [1,2,3,4,5]
print("Max :", max(numbers))
print("Min :", min(numbers))
print("Sum :", sum(numbers))
print("Len :", len(numbers))
print("All :", all(numbers))
print("All :", all([1,0,2]))
print("All :", all([1,"",'','sai']))
# %%
print("Any :", any(numbers))
print("Any :", any([1,0,'']))
print("Any :", any([0,False,'']))
# %%
numbers = [1,2,3,4,5,6,7,8,5]
print("Count",numbers.count(5))
print("Index",numbers.index(5))
# %%
numbers = [1,2,3,4,5,6,7,8,5]
print(4 in numbers)
print(10 in numbers)
print(10 not in numbers)
print()

# %%
list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)
# %%
list1=[1,2,3,4]
list2=[1,2,3]
print(list1==list2)
# %%
list1=[5,2,3]
list2=[1,2,3]
print(list1<list2)
# %%
list1=[5,2,3]
list2=[5,1,3]
print(list1>list2)
# %%
list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)
# %%
letters = ['a','b','c','d']
letters.append("x")
letters.append("y")
print(letters)
print()
# %%
letters = ['a','b','c','d']
letters.insert(0,'A')
letters.insert(1,'f')
print(letters)
# %%
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix.append(['x','y','z'])
matrix.insert(0,[1,2,3])
print(matrix)
# %%
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix[1].append('x')
matrix[0].insert(0,'z')
print(matrix)
# %%
letters = ['a','b','c','d']
letters.clear()
print(letters)
# %%
letters = ['a','b','c','d','b']
letters.remove('b')
letters.remove('b')
print(letters)
# %%
letters = ['a','b','c','d','b']
removed=letters.pop()
print(letters,"removed:",removed)
# %%
letters = ['a','b','c','d','b']
removed=letters.pop(1)
print(letters,"removed:",removed)
# %%
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix.remove(['a','b','c'])
matrix.pop()
print(matrix)
# %%
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix[1].remove('e')
matrix[1].pop(-1)
print(matrix)
# %%
letters = ['a','b','c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)
# %%
matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix[-1] = ['x','y','z'] 
matrix[0][0] = '-' 
print(matrix)
# %%
letters = ['c','a','b']
letters.sort()
print(letters)
# %%
letters = ['c','a','b']
letters.sort(reverse=True)
print(letters)
# %%
matrix=[ ['d','e','f'],
        ['a','b','c'],
        ['a','a','i']]
matrix.sort()
print(matrix)
# %%
letters = ['c','a','b']
new_list=sorted(letters)
print(new_list)
print(letters)
# %%
letters = ['c','a','b']
letters.reverse()
print(letters)
# %%
letters = ['c','a','b']
new_list=list(reversed(letters))
print(new_list)
print(letters)
# %%
letters = ['a','b','c']
letters_copy = letters
print("Original:",letters,id(letters))
print("Copy:",letters_copy,id(letters_copy))
# %%
letters = ['a','b','c']
letters_copy = letters
letters.append('z')
letters.pop(1)
print("Original:",letters,id(letters))
print("Copy:",letters_copy,id(letters_copy))
# %%
# %%
letters = ['a','b','c']
letters_copy = letters.copy()
print("Original:",letters,id(letters))
print("Copy:",letters_copy,id(letters_copy))
# %%
letters = ['a','b','c']
letters_copy = letters.copy()
letters.append('z')
letters.pop(1)
print("Original:",letters,id(letters))
print("Copy:",letters_copy,id(letters_copy))
# %%
matrix=[['a','b'],
        ['c','d']]
matrix_copy = matrix.copy()
matrix.pop()
print("Original:",matrix,id(matrix))
print("Copy:",matrix_copy,id(matrix_copy))
# %%
matrix=[['a','b'],
        ['c','d']]
matrix_copy = matrix.copy()
matrix_copy[0].append("z")
print("Original:",matrix,id(matrix))
print("Copy:",matrix_copy,id(matrix_copy))
# %%
import copy
matrix=[['a','b'],
        ['c','d']]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0].append("z")
print("Original:",matrix,id(matrix))
print("Copy:",matrix_copy,id(matrix_copy))
print("Same Object?:", matrix is matrix_copy)
# %%
letters = ['a','b','c','d']
numbers = [1,2,3]
comb = letters + numbers
print(comb)
print(letters * 2)
# %%
letters = ['a','b','c','d']
numbers = [1,2,3]
comb = [letters,numbers]
print(comb)

# %%
letters = ['a','b','c','d']
numbers = [1,2,3]
letters.extend(numbers)
print(letters)
# %%
letters = ['a','b','c']
numbers = [1,2,3]
comb =  list(zip(letters,numbers))
print(comb)
# %%
# %%
letters = ['a','b','c']
numbers = [1,2,3]
comb =  list(zip(letters,numbers,'Hi'))
print(comb)
# %%
