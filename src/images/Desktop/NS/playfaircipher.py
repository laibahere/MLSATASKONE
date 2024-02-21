def prepare_text(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I' since Playfair doesn't use 'J'
    text = text.replace("J", "I")

    # If the length of the text is odd, append an 'X' to make pairs
    if len(text) % 2 != 0:
        text += 'X'

    return text

def generate_key_square(key):
    # Create a 5x5 matrix for the key square
    key_square = [['' for _ in range(5)] for _ in range(5)]
    key = prepare_text(key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = "".join(sorted(set(key), key=key.index))

    row, col = 0, 0
    for letter in key:
        key_square[row][col] = letter
        col += 1
        if col == 5:
            col = 0
            row += 1

    return key_square

def find_position(key_square, letter):
    # Find the position of a letter in the key square
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == letter:
                return i, j

def encrypt_pair(key_square, pair):
    # Encrypt a pair of letters using Playfair cipher rules
    a, b = pair[0], pair[1]
    a_row, a_col = find_position(key_square, a)
    b_row, b_col = find_position(key_square, b)

    if a_row == b_row:
        return key_square[a_row][(a_col + 1) % 5] + key_square[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        return key_square[(a_row + 1) % 5][a_col] + key_square[(b_row + 1) % 5][b_col]
    else:
        return key_square[a_row][b_col] + key_square[b_row][a_col]

def playfair_encrypt(key, plaintext):
    plaintext = prepare_text(plaintext)
    key_square = generate_key_square(key)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        ciphertext += encrypt_pair(key_square, pair)

    return ciphertext

def decrypt_pair(key_square, pair):
    # Decrypt a pair of letters using Playfair cipher rules
    a, b = pair[0], pair[1]
    a_row, a_col = find_position(key_square, a)
    b_row, b_col = find_position(key_square, b)

    if a_row == b_row:
        return key_square[a_row][(a_col - 1) % 5] + key_square[b_row][(b_col - 1) % 5]
    elif a_col == b_col:
        return key_square[(a_row - 1) % 5][a_col] + key_square[(b_row - 1) % 5][b_col]
    else:
        return key_square[a_row][b_col] + key_square[b_row][a_col]

def playfair_decrypt(key, ciphertext):
    ciphertext = prepare_text(ciphertext)
    key_square = generate_key_square(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        plaintext += decrypt_pair(key_square, pair)

    return plaintext

# Example usage:
key = "KEYWORD"
plaintext = "LAIBA"
encrypted_text = playfair_encrypt(key, plaintext)
decrypted_text = playfair_decrypt(key, encrypted_text)

print("Original text:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
