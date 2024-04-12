import os
from pathlib import Path

ENCODING_DIR = Path(os.getcwd() +'\Encoding Test')

test_file = os.path.join(ENCODING_DIR, Path('text.txt'))
output_file_encode = os.path.join(ENCODING_DIR, Path('encoded.txt'))
output_file_decode = os.path.join(ENCODING_DIR, Path('decoded.txt'))

alphabet_hash = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 
                 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 
                 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

def encode(text):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') + 13) % 26
                encoded_char = alphabet_hash[index + 1]
                encoded_text += encoded_char
            elif char.isupper():
                index = (ord(char) - ord('A') + 13) % 26
                encoded_char = alphabet_hash[index + 1].upper()
                encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def decode(text):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') - 13) % 26
                decoded_char = alphabet_hash[index + 1]
                decoded_text += decoded_char
            elif char.isupper():
                index = (ord(char) - ord('A') - 13) % 26
                decoded_char = alphabet_hash[index + 1].upper()
                decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text

def save_encoded_content(encoded_content, output_file):
    with open(output_file, 'w') as f:
        f.write(encoded_content)

if __name__ == "__main__":
    choice = int(input("Encode: 1\nDecode: 2\nYour Choice: "))
    if choice == 1:
        with open(test_file) as file:
            original_content = file.read()
            print(f"Original Content:\n{original_content}")
            print("Encoding File...")
            encoded_content = encode(original_content)
            print(f"After Encoding:\n{encoded_content}")
            print("Saving encoded content to file...")
            save_encoded_content(encoded_content, output_file_encode)
    elif choice == 2:
        with open(output_file_encode) as file:
            original_content = file.read()
            print("Decoding File...")
            decoded_content = decode(original_content)
            print(f"After Decoding:\n{decoded_content}")
            print("Saving encoded content to file...")
            save_encoded_content(decoded_content, output_file_decode)