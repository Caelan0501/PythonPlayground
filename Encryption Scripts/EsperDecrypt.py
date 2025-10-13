#!/usr/bin/env python3
import argparse

#unused but might as well
def left_rotate_byte(n, d):
    return ((n << d) & 0xFF) | (n >> (8 - d))

#because was left shifted during encryption i need to go the other way
def right_rotate_byte(n, d):
    return ((n >> d) | ((n << (8 - d)) & 0xFF)) & 0xFF

def decrypt_with_key_and_rotate(cipher_bytes, key_string, rotate):
    key_bytes = [ord(c) for c in key_string] #Turn key into bytes
    out = bytearray(len(cipher_bytes)) #make a byte array
    #Xor then shift right
    for i, cb in enumerate(cipher_bytes):
        x = cb ^ key_bytes[i]
        out[i] = right_rotate_byte(x, rotate)
    return bytes(out)

#So I can change from the outside incase VM breaks network or something weird
p = argparse.ArgumentParser()
p.add_argument("-k", "--key", required=True)
p.add_argument("-r", "--rotate", type=int, required=False)
args = p.parse_args()

cyphertext = open("/challenge/ciphertext", "rb").read()
key = args.key
rotation = args.rotate
plaintext = decrypt_with_key_and_rotate(cyphertext, key, rotation)
with open("esper_plaintext.txt", "wb") as f:
    f.write(plaintext)
