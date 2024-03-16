import random

primefaclist = []
def generate_prime_factors(num2):
    global primefaclist
    n = num2 - 1
    primefaclist = [{} for _ in range(n)]

    for i in range(len(primefaclist)):
      if not primefaclist[i]:
        primefaclist[i][i+2] = 1
        pzanzahl = 1
        while (i+2)**pzanzahl <= num2:
          vielfache = 1
          while ((i+2) ** pzanzahl)*vielfache <= num2:
            primefaclist[((i+2) ** pzanzahl)*vielfache-2][i+2] = pzanzahl
            vielfache += 1
          pzanzahl += 1

user_input = input("Enter your command... (cmd [arg1] [arg2])")
user_input = user_input.lower()
user_input = user_input.split(" ")
op, num1, num2 = user_input
num1 = int(num1)
num2 = int(num2)


if op == "lpf":
  print("Genrating Primefactorisations..")
  generate_prime_factors(num2)
  num = []
  i = num1
  while i <= num2:
    num.append(i)
    i += 1
  print(num)
  while num:
    randomnumber = random.choice(num)
    rnstr = str(randomnumber)
    print("What's the prime factorization of", rnstr, "?" )
    answer = input()
    if answer == "Yes":
      num.remove(randomnumber)
  
  print("Congratulation, you're done!")

    
