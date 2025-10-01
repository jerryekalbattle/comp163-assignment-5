#Challenge 1: Number Sequence Generator
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")
# once its equal to 1 it will stop
while current_number != 1:
    if current_number >= 0:
        #means the number is even
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            #the number is odd
            current_number = (current_number * 3) + 1
        print(current_number, end=" ")
        # each loop counts this which then outputs step counts
        step_count += 1
print(f"\nSteps: {step_count}")
print()
# used zybooks exsamples to make sure i was on the right track
# im using while loop becuse i dont have a close guess of when it will end

# Challenge 2: Prime Number Checker
print("=== Challenge 2: Prime Number Checker ===")

n = int(input("Enter a number: "))

if n > 1:
    print(f"Testing divisors from 2 to {n - 1}...")
    for i in range(2, n - 1):
        if n % i == 0:
            print(f"{n} is not prime (divisible by 3)")
            break
    else:
        print(f"{n} is prime!")
else:
    print(f"{n} is not prime")
print()

# Challenge 3: Multiplication Table Grid
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("  ", end="")
# print header row
for header in range (1, 11):
    print(f"{header:4}", end="")
print()
for row in range (1, 11):
    print(f"{row:2}", end="")
    for column in range(1, 11):
        product = row * column
        print(f"{product:4}", end="")
    print()
# used ai for what :4 meeant because i didnt remember seeing it in zybooks