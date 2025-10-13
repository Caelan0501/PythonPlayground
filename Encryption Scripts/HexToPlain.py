def hex_to_text(hex_string: str) -> str:
    try:
        # Remove spaces or 0x prefixes, then decode
        hex_string = hex_string.replace(" ", "").replace("0x", "")
        bytes_data = bytes.fromhex(hex_string)
        return bytes_data.decode('utf-8', errors='replace')
    except ValueError:
        return "[Error: Invalid hex input]"

def main():
    hex_input = input("Enter hex string: ").strip()
    print("\nPlain text:", hex_to_text(hex_input))

if __name__ == "__main__":
    main()