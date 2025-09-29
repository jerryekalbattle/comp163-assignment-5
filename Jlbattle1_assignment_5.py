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


