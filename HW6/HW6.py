# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.

my_list_f = []

while True:
    text = input("Enter text ('a' to add, 'r' to remove, 'e' to exit): ")
    
    if text == "a":
        numb = int(input("Enter a number: "))
        my_list_f.append(numb)
    elif text == "r":
        numb = int(input("Enter a number: "))
        if numb in my_list_f:
            my_list_f.remove(numb)
        else:
            print("Number not found in the list.")
    elif text == "e":
        break  # აქ exit() რომ ვწერდი დანარჩენ კოდს აღარ უშვებდა
    else:
        print("Invalid input. Please enter 'a', 'r', or 'e'.")
    
    print(my_list_f)
    
    
        
# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას `my_list = [43, '22', 12, 66, 210, ["hi"]`, და შეასრულებს შემდეგ ნაბიჯებს:
my_list = [43, '22', 12, 66, 210, ["hi"]]
print(my_list)
#a. დაბეჭდავს `210`-ის ინდექსს;
print(my_list.index(210))
 
#b. დაამატებს ბოლო ელემენტში ტექსტს `"hello"`;
my_list.append("hello")
print(my_list)

#c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
del my_list[2]
print(my_list)

#d. შექმენით ახალი სია `my_llist_2`, რომელსაც ექნება `my_llist`-ის მნიშვნელობა, გაასუფთავეთ `my_llist_2`-ის მნიშნველობა და დაბეჭდეთ ორივე სია.
my_list_2 = my_list.copy()
print(my_list_2)
my_list_2.clear()
print(my_list_2)

# 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და 
# regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა  "(123) 456-789" ფორმატს, 
# თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

import re

pattern = r"\(\d{3}\) \d{3}-\d{3}"
phone_number = input("Enter telephone number")

if re.match(pattern, phone_number):
    print(phone_number) 
else:
    print("Invalid format") 
