# === Challenge 3: Multiplication Table ===
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
# Print header row (numbers 1 to 10)
print("   ", end="")  
x = 1
while x <= 10:
    print(f"{x:4}", end="")  
    x = x + 1
print()  

y = 1
while y <= 10:
    print(f"{y:2} ", end="")  
    z = 1
    while z <= 10:
        product = y * z
        print(f"{product:4}", end="")
        z = z + 1

    print()  
    y = y + 1
