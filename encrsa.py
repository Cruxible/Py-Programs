import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
	f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
	f.write(private_key.save_pkcs1("PEM"))

with open("public.pem", "rb") as f:
	public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
	private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "Hello World"

encrypted_message = rsa.encrypt(message.encode(), public_key)
with open("encrypted_message", "wb") as f:
	f.write(encrypted_message)
	print(encrypted_message)
'''
encrypted_message = open("encrypted_message", "rb").read()
print(encrypted_message)

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())
with open("clear_message", "wb") as f:
	f.write(clear_message)'''