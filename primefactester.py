import random
from sympy import factorint

user_input = input("Enter your command... (cmd [arg1] [arg2])")
user_input = user_input.lower()
user_input = user_input.split(" ")
op, num1, num2 = user_input
num1 = int(num1)
num2 = int(num2)

#print(num1)
if op == "lpf":
  #print(num1, num2)
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

    