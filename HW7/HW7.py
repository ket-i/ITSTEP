# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def fib_sequences (n):
    sequence = []  
    n1, n2 = 0, 1 
    count = 0
    while count <= n-1:
        n1, n2 = n2, n1+n2,
        count += 1
        sequence.append(n1)
    return(sequence)

print(fib_sequences(eval(input("Enter n number: "))))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები. 
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: `race` და `care` ანაგრამებია.

def fun_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(fun_anagrams("care", "race"))

# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for num in range(2, n + 1):
            fact = fact * num
        return fact
    

print(factorial(int (input ("Enter a number: "))))

# დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.

def fun_return_n (str3, symbol):
    return str3.count(symbol)

print(fun_return_n(input("Enter string: "), input("Enter Symbol: ")))

