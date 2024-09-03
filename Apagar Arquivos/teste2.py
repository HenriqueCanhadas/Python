import hashlib

password = "ambiental@365"
print(hashlib.sha256(password.encode()).hexdigest())
