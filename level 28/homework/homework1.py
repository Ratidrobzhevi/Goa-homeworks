# მომხმარებლისგან სამი წინადადების შეყვანა
sentence1 = input("Enter your sentence:")
sentence2 = input("Enter your sentence:")
sentence3 = input("Enter your sentence:")

# სტრინგის მეთოდების გამოყენება
print(sentence1.lower())       # 1. ყველა ასო პატარა
print(sentence2.upper())       # 2. ყველა ასო დიდი
print(sentence3.capitalize())  # 3. პირველი ასო დიდი, დანარჩენი პატარა


# მეორე ვარიანტი

sentence1 = "I LOVE GOAL ORIENTED ACADEMY"
sentence2 = "Goal Oriented Academy is the beast"
sentence3 = "Nika keshelava is Director of GOA"

print(sentence1.lower())       # i love goal oriented academy
print(sentence2.upper())       # GOAL ORIENTED ACADEMY IS THE BEAST
print(sentence3.capitalize())  # Nika keshelava is director of goa
