def shift_char(c: str, shift: int) -> str:
    return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))

def shift_string(text: str, shift: int) -> str:
    return ''.join(shift_char(c, shift) for c in text)

def brute_force(text: str):
    results = []
    for s in range(26):
        dec = shift_string(text, s)
        results.append((s, dec))
    return results

cyphertext = input('Cyphertext: ')

for i, plaintext in brute_force(cyphertext):
    print(f"[{i:2d}] {plaintext}")