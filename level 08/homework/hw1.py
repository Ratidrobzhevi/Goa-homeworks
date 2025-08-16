# 1)ჩაწერე განსხვავებული მონაცემთა ტიპების (int, float, string, boolean) ცვლადები.

number = 5 # int
float_num = 10.2 # float
name = "Rati" # str
is_adult = False # bool

# 2)მომხმარებელს შემოატანინეთ მისი ასაკი და type() ფუნქციით შეამოწმეთ,თუ რა ტიპის მონაცემია შემოტანილი ასაკი.

age = input("Please enter your age: ")

print(type(age))

# 3)მომხმარებელს შემოატანინეთ სახელი გვარი ასაკი სიმაღლე და გამოიტანეთ ეს ყველაფერი ერთ დიდ წინადადებაში.

firstname = input("Please enter your firstname: ")
lastname = input("Please enter your lastname: ")
age = input("Please enter your age: ")
height = input("Enter your height: ")

print("Hello,", firstname, lastname, ", I know you. You are", age, "years old and your height is", height, "sm")