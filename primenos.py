print("Enter a range of numbers")
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("The prime numbers in the range are:")
for num in range(start, end + 1):
    if num > 1:
        print(f"\nChecking {num}:")
        for i in range(2, int(num**0.5) + 1):
            print(f"  Trying divisor i={i}")
            if (num % i) == 0:
                print(f"    {num} is divisible by {i}, not prime.")
                break
        else:
            print(f"  {num} is prime!")
