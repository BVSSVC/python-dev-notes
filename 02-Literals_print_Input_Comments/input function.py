# By default input take string
language = input("Enter your language: ")
print("My first language is:", language)

total_marks = int(input("Enter the total number of marks: "))
print("My total_marks is :", total_marks)


a, b = map(str, input("Enter your values:").split())
print(a)
print(b)

a, b = map(int, input("Enter your values:").split())
print(a)
print(b)
