str1 = 'James'
print(str1[0]+str1[len(str1)//2]+str1[-1])

str1 = "JhonDipPeta"
print(str1[(len(str1)//2)-1:(len(str1)//2)+2])


s1 = "Ault"
s2 = "Kelly"
print(s1[:len(s1)//2]+s2+s1[(len(s1)//2)+1:])


str1='PyNaTive'
s1=''
s2=''
for i in str1:
    if i.islower():
        s1=s1+i
    elif i.isupper():
        s2=s2+i
new_string=s1+s2
print(new_string)

sample_str = "P@yn2at&#i5ve"
char_count=0
digit_count=0
symbol_count=0
for char in sample_str:
    if char.isalpha():
        char_count=char_count+1
    elif char.isnumeric():
        digit_count=digit_count+1
    else:
        symbol_count=symbol_count+1
print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

s1='Abc'
s2='xyz'
s1_length=len(s1)
s2_length=len(s2)

length = s1_length if s1_length > s2_length else s2_length
result=''
s2=s2[::-1]
for i in range(length):
    if i<s1_length:
        result+=s1[i]
    if i<s2_length:
        result+=s2[i]
print(result)
    
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"
temp=str1.lower()
count=temp.count(sub_string.lower())
print(count)
str1 = "PYnative29@#8496"
sum=0
count=0
for char in str1:
    if char.isnumeric():
        sum+=int(char)
        count+=1
average=sum/count
print(f"The sume is : {sum} and average is : {average}")

str1='apple'
char_dict=dict()
for char in str1:
    count=str1.count(char)
    char_dict[char]=count
print(char_dict)


str1="Pynative"
str1="".join(reversed(str1))
print(str1)

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

print("last occurence:",str1.rfind("Emma"))



import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)
new_str = str1.translate(str1.maketrans('','',string.punctuation))
print(new_str)

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

res="".join([item for item in str1 if item.isdigit()])
print(res)

str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
print(res)
for i in res:
    print(i)
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

for char in string.punctuation:
    str1=str1.replace(char,replace_char)
print(str1)
