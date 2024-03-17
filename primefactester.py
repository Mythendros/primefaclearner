import random

# Initialize an empty list to store dictionaries representing prime factors
primefaclist = []

# Function to generate prime factors up to a given limit
def generate_prime_factors(num2):
    global primefaclist
    # Calculate the range of numbers for which prime factors will be generated
    n = num2 - 1
    # Populate primefaclist with empty dictionaries, each representing prime factors for a number
    primefaclist = [{} for _ in range(n)]

    # Loop through each dictionary in primefaclist
    for i in range(len(primefaclist)):
        # If the dictionary is empty, indicating unprocessed number
        if not primefaclist[i]:
            # Add the number itself as a prime factor with a power of 1
            primefaclist[i][i+2] = 1
            pzanzahl = 1
            # Loop through powers of the prime factor
            while (i+2)**pzanzahl <= num2:
                vielfache = 1
                # Loop through multiples of the number and update prime factorization
                while ((i+2) ** pzanzahl)*vielfache <= num2:
                    primefaclist[((i+2) ** pzanzahl)*vielfache-2][i+2] = pzanzahl
                    vielfache += 1
                pzanzahl += 1

# Prompt user for input command
user_input = input("Enter your command... (cmd [arg1] [arg2])")
user_input = user_input.lower()
user_input = user_input.split(" ")
op, num1, num2 = user_input
num1 = int(num1)
num2 = int(num2)

# If command is to generate prime factorizations
if op == "lpf":
    print("Generating Prime Factorizations..")
    # Generate prime factorizations up to num2
    generate_prime_factors(num2)
    num = []
    i = num1
    # Create a list of numbers from num1 to num2
    while i <= num2:
        num.append(i)
        i += 1
    print(primefaclist)
    # Randomly select numbers from the list and prompt user for prime factorization
    while num:
        randomnumber = random.choice(num)
        rnstr = str(randomnumber)
        print("What's the prime factorization of", rnstr, "?" )
        answer = input()
        answer = answer.split(" ")
        primefac_answer = {}
        # Process user's input for prime factorization
        for x in answer:
            if len(x) == 1:
                primefac_answer[int(x)] = 1
            else:
                x = x.split("^")
                primefac_answer[int(x[0])] = int(x[1])
        # Check if user's answer matches the precomputed prime factorization
        if primefac_answer == primefaclist[randomnumber-2]:
            print("Correct!")
            num.remove(randomnumber)
        else:
            print("That's Wrong!")
  
    print("Congratulations, you're done!")
