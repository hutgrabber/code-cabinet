from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import io
import itertools
import hashlib
import os



UID = 119362914
First_Name="Sparsh"
Last_Name="Mehta"

key_with_error='''-----BEGIN DSA PRIVATE KEY-----
MIIBuQIBAAKBgQC973oUk7##7lilY1gwPAtXvTNDWbPbQhlstbax0b6LMyPCE1xf
gwLoercCPm1OWl65pRExUR5g0CJxFZNekWQKh7fNqzMQt5fUKMMwtU4Im05M+sTb
FeVYTiUrEdWjAbF5XvN6RgcEp7rL1ZX4VucElbxoAIvek+Aqfr0Zg/ltBQIVAKoK
+9q7j+T3esxgCTQMI2BQKSQnAn8dphjfU5jwzf+Nst9rkn1tZO0afBuzvNMRS8BF
9LCJ2q2Nly9Orifz8IJqkhIGnEy802QyjUgLJAgYlBWarK1vJTQApgwN3t66mE9J
Oc3gBgi9skZ/AQimaMb8YiHskbhn85ISpgJcvkjnL2KiTA/FtwTbzAj/Z5Sqv0xK
ax2GAoGBAJpAieRPdSlKrM7x5gVlPZiI5vXEdw83IBIsK0W5XTtD5LeDfemLQDO9
Qz49svcBuH6pdINnvQ3CrxaiJyJTMnfNNK9NuBeW2Q4KZJxQflXhcNuXcG0i2m0l
QizOAkzQKKHeIMk5+7KoD3tgm4xzJvPewhaSca6upI3xVUobnjs/AhR7SchExgXv
cJMj8CVGbPRdKkKBUg==
-----END DSA PRIVATE KEY-----
'''


def verify(key):
  try:
        possible_key = DSA.import_key(io.StringIO(key).getvalue())
        print("The key is correct :")
        print(key)
        return True
  except ValueError:
        return False


def bruteforce(key_with_error):

  key_with_error = list(key_with_error)
  permutations = itertools.product('abcdefghijklmnopqrstuvwxyz1234567890', repeat=2)
  
  for i in permutations:
      key_with_error[54], key_with_error[55] = i[0], i[1]
      new_key = ''.join(key_with_error)
      if(verify(new_key)):
          return new_key
      
plain1 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x87\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x71\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\xf2\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\xb4\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\xa8\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\x2b\x6f\xf7\x2a\x70'


#Incorrect inputblock
plain2 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x00\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x00\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\x72\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\x34\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\x28\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\xab\x6f\xf7\x2a\x70'


#Returns true if hashes match
def verify_hash(temp):
  return (hashlib.md5(plain1).digest()==hashlib.md5(temp).digest() and plain1 != temp)


def hash_collision(plain2):
  #WRITE CODE HERE

  permutations = itertools.product('0123456789abcdef', repeat=2)
  permutations = [''.join(i) for i in permutations]


  possible_hash = plain2 
  possible_hash = [hex(i)[2:].zfill(2) for i in possible_hash]
  
  
  for i in permutations:
    for j in permutations:
      for k in permutations:
        possible_hash[19], possible_hash[45], possible_hash[59] = i, j, k
        new_plain2 = bytes.fromhex(''.join(possible_hash))
        if(verify_hash(new_plain2)):
          return new_plain2

print("-------Bruteforcing key_with_error-------")
new_key = bruteforce(key_with_error)

print("------- Finding Collision -------")
print(f"Collision found at: \n{hash_collision(plain2)}")