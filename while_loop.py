##### Sum of even numbers ######
#sum_even = 0 
#i = 2
#n = int(input("Enter a number: "))
#while i <= n:
#    sum_even += i
 #   i += 2
#print(f"sum of even numbers from 1 to {n} is {sum_even}")


##### factorial calculation #####
#n = int(input("Enter a number: "))
#factorial = 1
#i = 1
#while i <= n :
    #factorial *= i
    #i += 1
#print(f"factorial of {n} is {factorial}")


##### Reverse a number #####
#n = int(input("Enter a number: "))
#reversed_num = 0
#while n>0:
    #reversed_num = (reversed_num*10) + n % 10
    #n = n//10
#print(f"reversed number is {reversed_num}")


#### Guess the number GAME #####
#import random

#target = random.randint(1,101)
#attempts = 0

#while True:
    #guess = int(input("Enter a number: "))
    #attempts += 1

    #if guess == target:
        #print(f"Congratulations! you have guessed the right number in {attempts} attempts")
        #break
    #elif guess < target:
        #print(f"Try a higher number")
    #else :
        #print(f"Try a lower number")


##### Palindrome Check #####
#n = input("Enter a number: ")
#reversed_num = 0
#i = len(n)
#while i > 0:
    #reversed_num = (reversed_num * 10)+ i % 10
    #i = i // 10
    #if i == reversed_num :
        #print(f"palindrome number.") 
    #else:
        #print("Not a palindrome")


##### FABONACCI SERIES #####
