# python program to implement Diffie-Helman Key Exchange 

import random

large_prime = 23
alpha = 5

# random numbers as private keys of A and B
Xa = random.randint(2, 10)
Xb = random.randint(2, 10)

print(f"A's secret key: {Xa}\nB's secret key: {Xb}")
 
# computing public (to-be shared) keys for A and B
Ya = pow(alpha, Xa)% large_prime
Yb = pow(alpha, Xb)% large_prime

print(f"A shares {Ya} to B\nB shares {Yb} to A")

# computing secret key obtained at both sides
Ka = pow(Yb, Xa) % large_prime
Kb = pow(Ya, Xb) % large_prime

if(Ka==Kb):
    print(f"Both parties got {Ka} as secret key!")
else:
    print("Something went wrong, different keys obtained!")