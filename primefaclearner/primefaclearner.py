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

# function to get the prime-factorisation of an integer as a human-readable string
def primefacstring(num):
    # get the primefactorisation as a dictionary
    dict = primefaclist[num-2]
    # create variable that gets returned
    output = ""
    # loop trough the different prime factors from the dictionary and add them to the string
    for pz in dict.keys():
        # check special case, if a prime factor is only once in the primefac
        if dict[pz] == 1:
            output = output + " " + str(pz)
        else:
            output = output + " " + str(pz) + "^" + str(dict[pz])
    # remove unecessary space at the beginning of the string
    output = output[1:]
    return output

# If command is to generate prime factorization
def quizme(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 < 2:
        num1 = 2
    if num2 < 2:
        num2 = 2
    if num1 > num2:
        num2 = num1
    generate_prime_factors(num2)
    num = []
    # Create a list of numbers from num1 to num2
    i = num1
    while i <= num2:
        num.append(i)
        i += 1
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
            if "^" not in x:
                primefac_answer[int(x)] = 1
            else:
                x = x.split("^")
                primefac_answer[int(x[0])] = int(x[1])
        # Check if user's answer matches the precomputed prime factorization
        if primefac_answer == primefaclist[randomnumber-2]:
            print("Correct!")
            num.remove(randomnumber)
            print(str(len(num)) + " numbers left to test.")
        else:
            print("That's Wrong! The prime factorisation is '" + primefacstring(randomnumber) + "'.")
            print(str(len(num)) + " numbers left to test.")
  
    print("Congratulations, you're done!")

def quizmereverse(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 < 2:
        num1 = 2
    if num2 < 2:
        num2 = 2
    if num1 > num2:
        num2 = num1
    generate_prime_factors(num2)
    num = []
    # Create a list of numbers from num1 to num2
    i = num1
    while i <= num2:
        num.append(i)
        i += 1
    # Randomly select numbers from the list and prompt user for prime factorization
    while num:
        randomnumber = random.choice(num)
        factorisationasstring = primefacstring(randomnumber)
        print("Which number does",factorisationasstring, "correspondend to?")
        answer = input()
        answer = int(answer)
        if answer == randomnumber:
            print("Correct!")
            num.remove(randomnumber)
            print(str(len(num)) + " numbers left to test.")
        else:
            print("That's Wrong! The corresponding number is '" + str(randomnumber) + "'.")
            print(str(len(num)) + " numbers left to test.")
  
    print("Congratulations, you're done!")

def showpf(num1, num2=None):
    num1 = int(num1)
    if num2 is None:
        generate_prime_factors(num1)
        print(num1,"=",primefacstring(num1))
    else:
        num2 = int(num2)
        if num1 < 2:
            num1 = 2
        if num2 < 2:
            num2 = 2
        if num1 > num2:
            num2 = num1
        generate_prime_factors(num2)
        num = []
        # Create a list of numbers from num1 to num2
        i = num1
        while i <= num2:
            num.append(i)
            i += 1
        for x in num:
            print(x,"=",primefacstring(x))


# End of the script
# End of the script
