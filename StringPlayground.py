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
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isspace())
print(s.isupper())
print(s.islower())
print(s.isascii())
print(s.isdecimal())
print(s.isprintable())
print(s.isnumeric())
print(s.isidentifier())
print(s.istitle())

print(s.split(" "))
#s = s.join("and exciting") #weird behaivor

print(s.encode())

#print(wordList)