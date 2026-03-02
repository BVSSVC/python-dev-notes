# By default PVM takes the numbers in decimal form(base-10).
a=10
b=0b1011
c=0o700
d=0x9af
print(a)
print(b)
print(c)
print(d)
# %%
# we can use bin() to convert to any base to binary.
decimal=10
octa=0o700
hexa=0x9af
print(bin(decimal))
print(bin(octa))
print(bin(hexa))

# %%
# we can use oct() to convert any case to octal form.
decimal=10
binar=0b1011
hexa=0x9af
print(oct(decimal))
print(oct(binar))
print(oct(hexa))
# %%
# we can use hex() to convert any case to hexa decimal form.
decimal=10
binar=0b1011
octa=0o700
print(hex(decimal))
print(hex(binar))
print(hex(octa))

