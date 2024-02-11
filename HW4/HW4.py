# 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.
print("task 1")
s = 0
n = eval (input("Enter a numer :"))

for i in range (1, n+1):
    s += i      
print(f"The sum of numbers from 1 to {n} is: {s}")


# 2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1
print("task 2")
m = eval (input("Enter a numer :"))
i = m + 1

while i != 1:
    i -= 1
    print (i)

# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.
print("Task 3")
import random

real_number = random.randint(0, 100)

while True:
    guess_number = eval(input("Enter a number: "))
    if guess_number == real_number:
        print(f"Congretulation, guess_number is {real_number}")
        break
    elif guess_number > real_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

print("Game is over")

# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. 
# შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. 
# ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.
print("task 4")
total_sum = 0

while True:
    number_x = input("Enter a number: ")
    if number_x == "sum":
        print(total_sum)
        break

    elif int(number_x) > 0:
        total_sum += int(number_x)

