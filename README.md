COMP 163 - Assignment 5: Loop Mastery

This assignment demonstrates mastery of Python loop structures (`while`, `for`, and nested loops) across three coding challenges. Each challenge explores different loop types and how they apply to real problems.

---
 Challenge 1: Collatz Conjecture (Number Sequence Generator)

Loop Type Used: `while` loop  
Reasoning:  
The `while` loop is used because the number of iterations is not known in advance. The Collatz sequence continues until the number reaches 1, so we need a loop that continues based on a condition rather than a fixed range.

How It Works: 
- The program takes a positive integer input.
- If the number is even, it is divided by 2.
- If it's odd, it's multiplied by 3 and 1 is added.
- The loop continues until the number becomes 1.
- Each number in the sequence is printed, and the total number of steps is counted and displayed.

---

 Challenge 2: Prime Number Checker

Loop Type Used: `for` loop  
Reasoning:  
A `for` loop is used because we know the exact range of values to check (from 2 to n-1). This makes the `for` loop ideal for iterating through a predictable range of numbers.

How It Works:
- The program takes a number greater than 1.
- It prints a message showing which divisors it is testing.
- A `for` loop checks every number from 2 to n-1.
- If any divisor divides the number evenly, the number is not prime.
- If no divisors are found, the number is declared prime.

---

 Challenge 3: Multiplication Table Grid

Loop Type Used: Nested `for` loops  
Reasoning:
Nested loops are necessary to create a 2D grid. The outer loop handles the rows, and the inner loop handles the columns in each row.

How It Works: 
- The program prints a formatted multiplication table from 1 to 10.
- The first row is the header (1 to 10).
- Each following row begins with the row number and prints the products of that row and each column (also 1 to 10).
- String formatting is used to align the output into a clean grid.

---

 AI Assistance Used

I used ChatGPT (OpenAI) to:
- Help format and debug output for exact spacing and alignment.
- Refactor my code to match test case expectations.
- Clarify loop usage and select the best loop type per challenge.

All logic and understanding of the problems were my own, with AI used only to improve structure, formatting, and output clarity.

