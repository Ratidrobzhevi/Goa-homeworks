# print() - ტექსტის ან რიცხვის გამოჩენა ეკრანზე
print("Hello, GOA!")  # => Hello, GOA!

# type() - გვეუბნება ცვლადის ტიპს (int, str, float და სხვა)
x = 5
print(type(x))  # => <class 'int'>

# str() - სხვა ტიპის მნიშვნელობას გადააქცევს სტრინგად
num = 123
print(str(num))  # => "123"

# int() - სტრინგს ან float-ს გადააქცევს მთელ რიცხვად
s = "25"
print(int(s))  # => 25

# float() - მთელ რიცხვს ან სტრინგს გადააქცევს ათწილადად
x = 10
print(float(x))  # => 10.0

# input() - მომხმარებლისგან იღებს ტექსტს
# name = input("Enter your name: ")
# print(name)

# len() - აბრუნებს სიგრძეს (რამდენი სიმბოლოა სტრინგში ან ელემენტი სიაში)
name = "Academy"
print(len(name))  # => 7

# range() - ქმნის რიცხვების მიმდევრობას (ხშირად გამოიყენება ციკლებში)
for i in range(3):
    print(i)  # => 0, 1, 2

# list() - ქმნის სიას
x = list("goa")
print(x)  # => ['g', 'o', 'a']
