def encrypt(S):
    if not S:
        return ""

    encrypted = []
    count = 1

    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            encrypted.append(S[i - 1] + str(count))
            count = 1

    encrypted.append(S[-1] + str(count))

    transformed = ''.join(encrypted)
    final_encrypted = transformed[::-1]

    return final_encrypted


def decrypt(encrypted_str):
    reversed_str = encrypted_str[::-1]

    decrypted = []
    i = 0
    while i < len(reversed_str):
        char = reversed_str[i]
        i += 1
        count_str = ''
        while i < len(reversed_str) and reversed_str[i].isdigit():
            count_str += reversed_str[i]
            i += 1
        count = int(count_str) if count_str else 1
        decrypted.append(char * count)

    return ''.join(decrypted)


# Example usage:
S1 = "aaaaaaaaaaaa"
encrypted_S1 = encrypt(S1)
decrypted_S1 = decrypt(encrypted_S1)
print(f"Input: {S1}")
print(f"Encrypted: {encrypted_S1}")
print(f"Decrypted: {decrypted_S1}")
print()

S2 = "ostad"
encrypted_S2 = encrypt(S2)
decrypted_S2 = decrypt(encrypted_S2)
print(f"Input: {S2}")
print(f"Encrypted: {encrypted_S2}")
print(f"Decrypted: {decrypted_S2}")