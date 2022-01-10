numbers = list (range(1,101))
for i in numbers:
    word = "процент"
    if 5 <= i <= 20 or 5 <= i % 10 <= 10 or i % 10 == 0:
        print (i, word + "ов")
    elif i % 10 == 1:
        print (i, word)
    elif i % 10 == 2 or 3 or 4:
        print(i, word + "а")
    