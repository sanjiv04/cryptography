# Python program to implement RSA algorithm
# RSA is an asymmetric algorithm, requiring public and private keys for encryption and decryption respectively. 

# function to find gcd
def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)


# key generation

# Step 1: generate or select two large unequal prime numbers
p, q = 5, 11

# Step 2: calculate n
n = p*q

# Step 3: calculate phi_n
phi_n = (p-1)*(q-1)

# Step 4: select integer e such that gcd(phi_n, e) = 1; 1<e<phi_n
e = 2
while e>1 and e<phi_n:
    if gcd(phi_n, e)==1:
        break
    else:
        e=e+1

# Step 5: Calculate d
d = 1
while ((d*e) % phi_n)!=1:
    d=d+1


pub_key = (e, n)
private_key = (d, n)

def encrypt(m, pu):
    return pow(m, pu[0])%pu[1]


def decrypt(c, pr):
    return pow(c, pr[0])%pr[1]



# encryption
m = 9  #message / plaintext
en = encrypt(m, pub_key)
print("Encrypted: ", en)

# decryption
dc = decrypt(en, private_key)
print("Decrypted: ", dc)
   



    