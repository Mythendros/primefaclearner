# primefaclearner
Primefaclearner is a Python script designed to help you memorize prime factorizations. It can efficiently generate prime factorizations for numbers within a specified range and quiz you about them.

## Installation
```
pip install "????"
```

## Input
**1st Input: cmd [arg1] [arg2]**

cmd is the command to excecute:

1. quizme: This command quizes the user about prime factorizations in a given range
2. showpf: This command gives the prime factorization of a given number

*Sidenote*: It must be a string representing a valid command.

### quizme
*First input*: quizme [arg1] [arg2]

[arg1]: This is the first argument, which is expected to be an integer representing a lower bound.

[arg2]: This is the second argument, which is expected to be an integer representing an upper bound. 

For example, a valid command would be:

```
quizme 37 56
```
This would let the program generate all prime factorizations between 37 and 56.

*2nd Input*: Prime factorization of the number

Make sure your answer follows this format: `prime^power`, with each prime factor and its power separated by a space, and multiple prime factors separated by a space as well.

For example, if the program asks for the prime factorization of the number 12, you would respond with the prime factors and their powers:

```
2^2 3
```

This answer indicates that the prime factorization of 12 is \(2^2 times 3\), meaning that 2 is raised to the power of 2 and 3 is raised to the power of 1. 

### showpf
*First input*: showpf [arg1]

[arg1]: This Input represents the number that is taken to generate the prime factorization.
