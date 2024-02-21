def encrypt_rail_fence(plaintext, rails):
    cipher_text = ['' for _ in range(rails)]
    current_row = 0
    direction = 1  # 1 for downward, -1 for upward

    for char in plaintext:
        cipher_text[current_row] += char
        current_row += direction

        if current_row == 0 or current_row == rails - 1:
            direction *= -1

    return ''.join(cipher_text)


def decrypt_rail_fence(ciphertext, rails):
    decrypted_text = ['' for _ in range(rails)]
    current_row = 0
    direction = 1
    char_index = 0

    for _ in range(len(ciphertext)):
        decrypted_text[current_row] += ciphertext[char_index]
        char_index += 1
        current_row += direction

        if current_row == 0 or current_row == rails - 1:
            direction *= -1

    return ''.join(decrypted_text)


# Example usage:
plaintext = "HelloWorld"
rails = 3

# Encryption
encrypted_text = encrypt_rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
