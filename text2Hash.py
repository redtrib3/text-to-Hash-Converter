import hashlib

def md5hash():
    user = str(input("Enter text to Hash(MD5 HASH):"))
    print("String   ----->",user)
    result = hashlib.md5(user.encode())
    result = result.hexdigest()
    print("MD5 hash ----->",result)

def sha256hash():
    user = str(input("Enter text to Hash(SHA256):"))
    print("String  ----->",user)
    result1 = hashlib.sha256(user.encode())
    result1 = result1.hexdigest()
    print("SHA256 ------>",result1)

def sha384hash():
    user = input("Enter text to Hash (SHA384):")
    print("String  ------>",user)
    result2 = hashlib.sha384(user.encode())
    result2 = result2.hexdigest()
    print("SHA384  ------>",result2)

def sha224hash():
    user = input("Enter text to Hash (SHA224):")
    print("String   ----->",user)
    result3 = hashlib.sha224(user.encode())
    result3 = result3.hexdigest()
    print("SHA224   ----->",result3)

def sha512hash():
    user = input("Enter text to hash(SHA512):")
    print("String   ----->",user)
    result4 = hashlib.sha512(user.encode())
    result4 = result4.hexdigest()
    print("SHA512   ----->",result4)

def sha1hash():
    user = input("Enter your text to Hash(SHA1):")
    print("String    ----->",user)
    result5 = hashlib.sha1(user.encode())
    result5 = result5.hexdigest()
    print(" SHA1     ----->".result5)

def blake2bhash():
    user = input("Enter your text to Hash(blake2b):")
    print("String    ------>",user)
    result6 = hashlib.blake2b(user.encode())
    result6 = result6.hexdigest()
    print("Blacke2b  ------->",result6)




print("\nWELCOME TO TEXT 2 HASH CONVERTER !\n\nSELECT A HASH AlGORITHM:")
print("""

|-----|------------------------|
|Sl.no|  A L G O R I T H M S   |
|-----|------------------------|
|1 .  | MD5 Hash algorithm     |
|2 .  | SHA256 Hash algorithm  |
|3 .  | SHA384 Hash algorithm  |
|4 .  | SHA224 Hash algorithm  |
|5 .  | SHA512 Hash algorithm  |
|6 .  | SHA-1 Hash algorithm   |
|------------------------------|


""")

guy = str(input("select by number >>>>>"))

if guy == "1":
    md5hash()
elif guy == "2":
    sha256hash()
elif guy == "3":
    sha384hash()
elif guy == "4":
    sha224hash()
elif guy == "5":
    sha512hash()
elif guy == "6":
    sha1hash()

else:
    print("are you drunk ? select a valid number ! ")
