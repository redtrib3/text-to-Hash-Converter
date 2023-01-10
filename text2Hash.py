import hashlib


print("\nTEXT 2 HASH CONVERTER !\nSelect an Hashing Algorithm:")
print("""

+-----+------------------------+
|Sl.no|  A L G O R I T H M S   |
|-----+------------------------+
|1    | MD5 Hash algorithm     |
|2 .  | SHA256 Hash algorithm  |
|3 .  | SHA384 Hash algorithm  |
|4 .  | SHA224 Hash algorithm  |
|5 .  | SHA512 Hash algorithm  |
|6 .  | SHA-1 Hash algorithm   |
+-----+------------------------+


""")

guy = int(input("Algorithm >> "))
hashlst = [hashlib.md5, hashlib.sha256, hashlib.sha384, hashlib.sha224, hashlib.sha512, hashlib.sha1]

user = input("Enter text to hash: ")
res = hashlst[ guy - 1 ](user.encode()) 
res = res.hexdigest()


print(f"Hash --->",res)
