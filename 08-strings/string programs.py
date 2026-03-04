text="""
python is easy to learn.
python is powerful
Many people love python
"""
print(text.count('python'))

# tranformations
price="12345,67"
print(price.replace(',','.'))
phone="166-1234-566"
print(phone.replace('-','/'))
phone="166-1234-566"
print(phone.replace('-',''))
phone="166-1234-566,123"
print(phone.replace('-','/').replace(",",""))

firstname='Michael'
last_name="Scott"
print(firstname+last_name)
print(firstname+' '+last_name)

folder="C:/Users/bsaiv"
file="strings.ipynb"
full_folder_path=folder+'/'+file
print(full_folder_path)

my_details="Sai Vardhan-24-INDIA"
print(my_details.split("-"))
csv_file="saivardhan,24,India,Male"
print(csv_file.split(","))

print("ha" * 3)
print("----------")
print("-"*10)

a,b,c,d,e="hello"
print(a)
print(b)
print(c)
print(d)
print(e)


text = "Python"
print(text[-6])
print(text[5])
print(text[-1])
print(text[3])


date="2026-12-26"
print(date[0:4])
print(date[:4])
print(date[5:7])
print(date[8:])
print(date[-2:])

text="  Engineering"
print(text.lstrip())
text="Engineering  ".rstrip()
print(text)
text="    Engineering  ".strip()
print(text)
text="  Data  Engineering  ".strip()
print(text)
text="###ABC###".strip("#")
print(text)
text="    Engineering  "
print(len(text))
print(len(text.strip()))
nr_of_spaces=len(text)-len(text.strip())
is_clean=len(text)==len(text.strip())
print("Nr of spaces:",nr_of_spaces)
print("Is my data clean?",is_clean)


text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

search = "Email"
data = "email"
print(search == data)
search = "Email".lower()
data = "email".lower()
print(search == data)

search = "Email ".lower().strip()
data = "email".lower().strip()
print(search == data)

text='968-Maria, ( D@t@ Engineer );; 27y..'
s = text.rstrip(".; ")
print(s)
before_comma,after_comma=s.split(",",1)
print(before_comma)
print(after_comma)
emp_id,name=before_comma.split("-")
print(emp_id,type(emp_id))
print(name)
print(after_comma)
role_part = after_comma.split(")")[0]   # take until ')'
role=role_part.replace("(","").strip()
role = role.replace("@", "a").title()
print(role)
age_part = after_comma.split(")")[-1].strip()
age_part=age_part.replace(";","").strip()
age = age_part.replace("y", "").strip()
age = int(age)
print(age)
result = {
    "id": emp_id,
    "name": name,
    "role": role,
    "age": age
}

print(result)

phone="+1612-203-9658"
print(phone.startswith("+1"))
phone="+1612-203-9658"
print(phone.startswith("+91"))

email='bsaivardhan7@gmail.com'
print(email.endswith("@gmail.com"))

file="data_backup.csv"
print(file.endswith(".csv"))


print("@" in email)

url = 'https://api.company.com/v1/date'
print("api" in url)


phone1="+1612-203-9658"
print(phone.find("-"))
print(phone[phone.find("-")+1:])


country = "USA"
print(country.isalpha())

country = "USA1"
print(country.isalpha())


phone = "61222039658"
print(phone.isnumeric())


phone = "6122203965-8"
print(phone.isnumeric())