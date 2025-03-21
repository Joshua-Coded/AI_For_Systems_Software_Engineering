# Looping  checks
# Loop through a list of items

# fruits = ["Apple", "Banana", "Cherry"]

# for fruit in fruits:
#     print(fruit)
    
# for i in range(5):
#     print(i)
    
# While Loop
# create a count down to 5

# count = 5

# while count > 0:
#     print(count)
#     count -= 1
    
# print("Outside while Loop")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
        
       
       
# check if a given number is a prime number (if it is not divisible by 2)

# num = int(input("Enter a number: "))


# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime")
#             break
#         else:
#             print(f"{num} is a prime")


# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     if b != 0:
#      return a // b
    
#     else:
#         return "Division by zero is not allowed" 
    
    
# while True:
#     print("\nMenu:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4 Division")
#     print("5. Exit")
    
#     choice = input("Enter choice from the menu")
    
#     if choice == "5":
#         print("Exitin program")
#         break
    
#     num1 = float(input("Enter the first number"))
#     num2 = float(input("Enter the second number"))
    
#     if choice == "1":
#         print("Result:", add(num1. num2))
#     elif choice == "2":
#         print("Result:", sub(num1, num2))
#     elif choice == "3":
#         print("Resutl: ", mul(num1, num2))
#     elif choice == "4":
#         print("Result: ", div(num1, num2))
#     else:
#         print("Invalid choice:. please try again")
    