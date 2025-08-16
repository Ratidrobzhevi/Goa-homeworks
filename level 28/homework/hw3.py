my_name = "Rati"  # ცვლადში შენახულია ჩემი სახელი

user_name = input("Enter your name:")

# ვადარებთ სახელებს პატარა ასოებით
if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")