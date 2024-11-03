import rsa

publicKey, privateKey = rsa.newkeys(512)

def encrypt_file(file_path, public_key):
    # reads the file contents
    with open(file_path, 'rb') as f:
        file_content = f.read()

    # encrypts the file contents
    enc_content = rsa.encrypt(file_content, public_key)

    # writes the encrypted content to a new file
    with open(file_path + '.enc', 'wb') as f:
        f.write(enc_content)

    print(f"File '{file_path}' encrypted successfully to '{file_path}.enc'.")

def decrypt_file(enc_file_path, private_key):
    # reads the encrypted file content
    with open(enc_file_path, 'rb') as f:
        enc_content = f.read()

    # decrypts the content
    dec_content = rsa.decrypt(enc_content, private_key)

    # writes the decrypted content to a new file
    dec_file_path = enc_file_path.replace('.enc', '_decrypted')
    with open(dec_file_path, 'wb') as f:
        f.write(dec_content)

    print(f"File '{enc_file_path}' decrypted successfully to '{dec_file_path}'.")


if __name__ == "__main__":
    # encrypt the file
    original_file = "test.txt"  
    encrypt_file(original_file, publicKey) 

    # decrypt the file
    encrypted_file = original_file + '.enc'
    decrypt_file(encrypted_file, privateKey) 