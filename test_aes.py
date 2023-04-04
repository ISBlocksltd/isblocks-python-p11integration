import os
import pkcs11


try:
	lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
except KeyError:
    raise RuntimeError("Must define `PKCS11_MODULE' to run tests.")


print("get pkcs11 token")
token = lib.get_token(token_label='partition01')




# Open a session on our token
with token.open(user_pin='1234567') as session:
    # Generate an AES key in this session
    print("generate AES key ")
    key = session.generate_key(pkcs11.KeyType.AES, 256)
    
	
    data = b'INPUT DATA'
    print("data to compute ", data)
	
	
    # Get an initialisation vector
    iv = session.generate_random(128)  # AES blocks are fixed at 128 bits
    print("IV ", iv)
	
	
    # Encrypt our data
    crypttext = key.encrypt(data, mechanism_param=iv)
    print("Encrypted data ", crypttext)

    # decrypt our data
    decrypttext = key.decrypt(crypttext, mechanism_param=iv)
    print("decrypted data ", decrypttext)
