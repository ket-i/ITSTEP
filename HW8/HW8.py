#  შექმენით გლობალური ცვლადი `int_list = [10,20,30,40]` და 
# დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ `int_list` სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10,20,30,40]

def func_1(n):
    global int_list 
    return int_list.append(n)

# print(int_list)
# func_1(eval(input("Enter number: ")))
# print(int_list)

# 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. 
# პარამეტრად უნდა მიიღოს შემდეგი სია `[100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]`.

numbers_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def calculate_sum(numbers):
    return sum(numbers)

result_new_list = calculate_sum(numbers_list)
print(result_new_list)

# 3. შექმენით გლობალური ცვლადი `gl_str = "Global"` და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს  `(gl_str)` და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

gl_str = "Global"

def retuen_local_variable():
    gl_str = "Local"
    return gl_str

print(gl_str)

local_var = retuen_local_variable()
print( local_var)

# 4 რეკურსიის გამოყენებით  დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს `number` და
#  დააბრუნებს  ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი `12345`, უნდა დააბრუნოს `15`. რადგან `1+2+3+4+5`  უდრის `15`-ს).

def return_sum (number):
    if number < 10:
        return number
    else:
        return number % 10 + return_sum(number // 10)

input_number = 12345
result_sum = return_sum(input_number)
print(result_sum)

# 5 რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, 
# რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  `input: Hello   Output: olleH`)

def reverse_string(string):
   if len(string) == 0:
       return "" 
   else:
       return reverse_string(string[1:]) + string[0]

reversed_string = reverse_string("Hello")
print(reversed_string)

