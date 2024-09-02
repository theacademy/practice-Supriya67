import secrets
import string
n=int(input("Enter the length of password req:"))
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(n))
print(password)