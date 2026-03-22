def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

u, l = count_case("Hello World")
print("Uppercase:", u, "Lowercase:", l)
