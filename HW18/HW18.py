#Task 1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
         return Vector(self.x + other.x, self.y + other.y)
        
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

# Example:
    
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)


#Task 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Example
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False





