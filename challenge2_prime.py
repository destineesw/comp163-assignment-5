print("=== Challenge 2: Prime Number Checker ===")

n = int(input("Enter a number: "))

if n <= 1:
    print("Number must be greater than 1.")
else:
    print("Testing divisors from 2 to", n - 1, "...")
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime (divisible by", i, ")")
            is_prime = False
            break

    if is_prime:
        print(n, "is prime!")
