def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage
plaintext = "HELLO WORLD"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
decrypted_text = caesar_decrypt(ciphertext, shift)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
