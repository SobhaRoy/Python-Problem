def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print("HCF:", hcf(12, 18))
