# 1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და
# zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

def zip_function(*lists):
    print(list(zip(*lists)))


arr1 = [1, 2, 3]
arr2 = ["a", "b", "c"]

zip_result = zip_function(arr1, arr2)
print(zip_result)

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. 
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).

from functools import reduce

def element_product(list1):
    try:
        product = reduce(lambda x, y: x * y, list1, 1)
        return product
    except TypeError as e:
        print("TypeError occurred:", e)

print(element_product([1, 2, 3]))

# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

def odd_fun(*list3):
    odd_numbers = filter (lambda x : x % 2 != 0, *list3) 
    return odd_numbers


print(list(odd_fun([1,2,3,4,5])))

# 4 . დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
def ending_fun (list4, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), list4))
        return filtered_list
    except TypeError as e:
        raise TypeError("Incorrect type")
    
print(ending_fun(['hello', 'world', 'coding', 'nod'], "ing"))
    


