s = "Helldivers is fun"

# String Manipulation Functions
#Upper and Lowercases
print(s.capitalize()) # Alphabetical character at index 0 is uppercased
print(s.upper())      # All Alphabetical characters are uppercased
print(s.lower())      # All Alphabetical characters are lowercased
print(s.swapcase())   # All Alphabetical characters are Swapped cases
print(s.title())      # First letter of every word is uppercased
print(s.casefold())   # More aggressive form of lower allowing for more characters lowercased

# String Boolean Checking
print(s.isalpha())    #Contains only Alphabetical characters
print(s.isupper())      #Contains only Uppercase characters
print(s.islower())      #Contains only Lowercase characters
print(s.istitle())      #Is title case
print(s.isnumeric())
print(s.isdigit())
print(s.isdecimal())
print(s.isalnum())
print(s.isascii())
print(s.isprintable())
print(s.isspace())
print(s.isidentifier())
print(s.endswith("fun"))
print(s.startswith("Helldivers"))

#String Changing
print(".".join(s)) #weird behaivor
print(s.encode())
print(s.replace("Helldivers","Hello"))
print(s.count("Helldivers"))

print(s.ljust(30, "s"))
print(s.rjust(30, 's'))
print(s.center(30, 's'))
print(s.zfill(30))
print(s[2:len(s)-1])
print(s[:5])
print(s[5:])
print(s[-5:-2])

print(("    " + s + "   ").expandtabs())

print((" " + s + " ").strip())
print(s.lstrip())
print(s.rstrip("Helldivers"))

print(s.find("Helldivers"))
print(s.rfind("Helldivers"))
print(s.index("Helldivers"))
print(s.rindex("Helldivers"))

print(s.split(" "))
print(s.rsplit(" "))
print(s.partition(" "))
print(s.rpartition(" "))

print(s.removeprefix("Helldivers"))
print(s.removesuffix("fun"))

print(len(s))
print(s + s)
print('''Helldivers
is
fun''')

sn = "Helldivers {num} is fun"
print(sn.format(num = 2))
num = 2
sf = f"Helldivers {num} is fun"
print(sf)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# input stored in variable a.
a = {'x':'John', 'y':'Wick'}

# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))