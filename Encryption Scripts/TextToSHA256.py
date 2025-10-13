import hashlib

text = input("Enter text: ")
hash_object = hashlib.sha256(text.encode())
hex_dig = hash_object.hexdigest()

print("SHA256 Hash:" + hex_dig)