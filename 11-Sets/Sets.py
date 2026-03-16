# %%
my_set = {'a','b','c',True,100}
print(my_set,type(my_set),id(my_set))
# %%
my_book_set = set(('Harry Potter', 'Dungeons & Dragons', 'Atlas Shrugged'))
print(my_book_set,type(my_book_set),id(my_book_set))
# %%
# list with duplicate items
number_list = [20, 30, 20, 30, 50, 30]
# create a set from a list
sample_set = set(number_list)
print(sample_set)
# %%
# set of mutable types
sample_set = {'Mark', 'Jessa', [35, 78, 92]}
print(sample_set)
# Output TypeError: unhashable type: 'list' [35, 78, 92]
# %%
empty_set = set()
print(empty_set,type(empty_set))
# %%
emptySet = {}
print(type(emptySet)) # class 'dict'
# %%
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
for book in book_set:
    print(book)
# %%
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
if 'Harry Potter' in book_set:
    print("Book exists in the book set")
else:
    print("Book doesn't exists in the book set")
print("A man in Love" in book_set)
# %%
# create a set using set constructor
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
print(len(book_set))
# %%
book_set = {'Harry Potter', 'Angels and Demons'}
# add() method
book_set.add('The God of small things.')
print(book_set)
book_set.update(["Alice in wonder Land","Wings of fire"])
print(book_set)
# %%
color_set = {'red', 'orange', 'yellow', 'white', 'black'}
color_set.remove('red')
print(color_set)
color_set.remove('black brown')
print(color_set)
# %%
color_set = {'red', 'orange', 'yellow', 'white', 'black'}
color_set.remove('red')
print(color_set)
color_set.discard('black brown')
print(color_set)
# %%
color_set = {'red', 'orange', 'yellow', 'white', 'black'}
color_set.pop()
print(color_set)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set | remaining_colors
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set.union(remaining_colors)
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set & remaining_colors
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set.intersection(remaining_colors)
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
color_set.intersection_update(remaining_colors)
print(color_set)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set - remaining_colors
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set.difference(remaining_colors)
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
color_set.difference_update(remaining_colors)
print(color_set)
# %%
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set ^ remaining_colors
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
vibgyor = color_set.symmetric_difference(remaining_colors)
print(vibgyor)
# %%
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
color_set.symmetric_difference_update(remaining_colors)
print(color_set)
# %%
color_set1 = {'violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red'}
color_set2 = {'indigo', 'orange', 'red'}
print(color_set1.issubset(color_set2))
print(color_set2.issubset(color_set1))
# %%
color_set1 = {'violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red'}
color_set2 = {'indigo', 'orange', 'red'}
print(color_set1.issuperset(color_set2))
print(color_set2.issuperset(color_set1))
# %%
color_set1 = {'violet', 'blue', 'yellow', 'red'}
color_set2 = {'orange', 'red'}
color_set3 = {'green', 'orange'}
print(color_set2.isdisjoint(color_set1))
print(color_set3.isdisjoint(color_set1))
# %%
rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
# create a frozenset
f_set = frozenset(rainbow)

print(f_set)
# output frozenset({'green', 'yellow', 'indigo', 'red', 'blue', 'violet', 'orange'})
# %%
rainbow = ('violet', 'indigo', 'blue')
f_set = frozenset(rainbow)
# Add to frozenset
f_set.add(f_set)
# output AttributeError: 'frozenset' object has no attribute 'add'
# %%
