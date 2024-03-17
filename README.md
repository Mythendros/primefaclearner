# primefaclearner
Primefaclearner is a Python script designed to efficiently generate prime factorizations for numbers within a specified range. The user is prompted to guess the prime factorization of a randomly selected number within the given range.

**1st Input: cmd [arg1] [arg2]**
cmd is the command to excecute:
1. lpf: This command indicates that the program should generate prime factorizations.
  
[arg1]: This is the first argument, which is expected to be an integer representing a lower bound or a starting number depending on the operation.

[arg2]: This is the second argument, which is expected to be an integer representing an upper bound or a limit depending on the operation.

So, the criteria for the first input are:

- It must be a string representing a valid command (`lpf` in this case).
- It must be followed by two integers separated by spaces, representing the range or limits for the operation.

**2st Input: Prime factorization of the number**

When the program prompts you for the prime factorization of a number, your answer should provide the prime factors along with their respective powers. Here's an example of how you could format your answer:

For example, if the program asks for the prime factorization of the number 12, you would respond with the prime factors and their powers:

```
2^2 3^1
```

This answer indicates that the prime factorization of 12 is \(2^2 \times 3^1\), meaning that 2 is raised to the power of 2 and 3 is raised to the power of 1. 

Make sure your answer follows this format: `prime^power`, with each prime factor and its power separated by a space, and multiple prime factors separated by a space as well.
