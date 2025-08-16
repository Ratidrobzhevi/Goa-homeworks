# ორიგინალი სტრინგი
text = "Hello, World!"

# "Hello" ამოჭრა (სფეისისა და მძიმის გარეშე)
hello = text[0:5]

# "World!" ამოჭრა (დავიწყოთ მე-7 ინდექსიდან, რადგან 6-ზე არის სფეისი)
world = text[7:]

# ბეჭდვა ტერმინალში სასურველი თანმიმდევრობით
print(text)        # Hello, World!
print(hello)       # Hello
print(world)       # World!
