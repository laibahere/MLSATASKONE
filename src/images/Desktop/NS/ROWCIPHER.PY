import math

def encrypt_row_transposition(plaintext, key):
    num_columns = len(key)
    num_rows = math.ceil(len(plaintext) / num_columns)

    # Create an empty matrix
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the matrix row-wise with the characters of the plaintext
    index = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if index < len(plaintext):
                matrix[i][j] = plaintext[index]
                index += 1

    # Sort the rows based on the key
    sorted_matrix = [list(row) for _, row in sorted(zip(key, matrix))]

    # Concatenate the columns to obtain the encrypted text
    encrypted_text = ''.join([''.join(row) for row in sorted_matrix])
    return encrypted_text

def decrypt_row_transposition(ciphertext, key):
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)

    # Create an empty matrix
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the matrix column-wise with the characters of the ciphertext
    index = 0
    for j in range(num_columns):
        for i in range(num_rows):
            if index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    # Arrange the rows based on the inverse of the key
    inverse_key = sorted(range(len(key)), key=lambda k: key[k])
    sorted_matrix = [list(row) for _, row in sorted(zip(inverse_key, matrix))]

    # Concatenate the rows to obtain the decrypted text
    decrypted_text = ''.join([''.join(row) for row in sorted_matrix])
    return decrypted_text

# Example usage:
plaintext = "LAIBA"
key = [2, 1, 3]

# Encryption
encrypted_text = encrypt_row_transposition(plaintext, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_row_transposition(encrypted_text, key)
print("Decrypted:", decrypted_text)
