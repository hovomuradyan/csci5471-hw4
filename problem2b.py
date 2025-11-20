import math
import hashlib

def discrete_log(g, h, p):
    """
    Compute discrete logarithm: find x such that g^x ≡ h (mod p)
    using baby-step giant-step algorithm
    """
    m = int(math.ceil(math.sqrt(p - 1)))
    # Baby steps
    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * g) % p
    # g^(-m) mod p
    g_inv_m = pow(g, p - 1 - m, p)
    # Giant steps
    current = h
    for i in range(m):
        if current in baby_steps:
            return i * m + baby_steps[current]
        current = (current * g_inv_m) % p
    return None

def main():
    p = 2**31 - 1
    g = 7
    n = 106401427
    print(f"Computing discrete log: {g}^x ≡ {n} (mod {p})")
    result = discrete_log(g, n, p)
    if result is not None:
        print(f"Solution found: x = {result}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
