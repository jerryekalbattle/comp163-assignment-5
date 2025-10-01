
Challenge 1: Collatz Conjecture

Why I chose a while loop:
The Collatz sequence continues until the number reaches 1, but there is no way to know how many steps that it will take. A while loop is the best fit because it runs until a condition is met (current_number != 1).

How it works:

The program takes a starting number from the user. If the number is even, it is divided by 2. If the number is odd, it is replaced with (current_number * 3) + 1. This repeats until the number becomes 1. The sequence and the number of steps are printed.

Challenge 2: Prime Number Checker

Why I chose a for loop:
A for loop because the number of iterations is known ahead of time.

How it works:
The program asks the user for a number. If the number is greater than 1, it tests divisibility. If the number is divisible by any integer in the range, it is not prime. If no divisors are found, the number is prime.

Challenge 3: Multiplication Table

Why I chose nested for loops:
The multiplication table has a fixed size. Each row and column must be calculated systematically. Two for loops make it simple: one for rows, and one nested loop for the columns inside each row.

How it works:

The header row (1–10) is printed first. For each row, the row label is printed. For each column, the product of row × column is calculated and displayed with spacing for alignment.

AI Assistance

I used AI assistance (ChatGPT) for clarifying the purpose of the :4. The rest i mostly used zybooks and exsamples drom class.
