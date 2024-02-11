# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

import base64

st = str(input("Enter a string: "))

st_b64 = base64.b64encode(st.encode('utf-8'))
print(st_b64)


# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

st_1 = str(input("Enter a string: ")).strip().lower()+"Python"

print(st_1.replace("python","Python"))

# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.
st_2 = str(input("Enter a string: "))

half_len = len(st_2)//2

print(st_2[:half_len])

# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. სტრიქონი ვალიდურია მაშინ, 
#როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)

import string

st_3 = input("Enter text: ")

if any(char.isdigit() for char in st_3) and all(char not in string.punctuation for char in st_3):
    print("Valid")
else:
    print("Not Valid")

# 5  დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, 
    #ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.   
     
import base64

st_4 = input("Enter a string: ")

st_b64 = base64.b64encode(st_4.encode('utf-8'))
print(st_b64)

st = base64.b64decode(st_b64).decode('utf-8')
print(st)


