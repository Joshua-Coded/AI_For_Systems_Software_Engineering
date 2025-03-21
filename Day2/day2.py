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

num = int(input("Enter a number: "))


if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime")
            break
        else:
            print(f"{num} is a prime")
