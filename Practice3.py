# x = int(input("Enter the number: "))
x = 2
if x > 200:
    print("x is greater.")
else:
    print("x is smaller")

# string slicing
# Strings are immutable, changed strings can be stored in new string
a = "Rimi"
print(a[-4:-2])

str = " Hello this is Rimi Singh ^_^  "
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.strip())              #removes space from front
print(str.rstrip())
print(str.replace("Rimi", "Simi"))
print(str.isalpha())
print(str.isalnum())
print(str.find("Rimi"))