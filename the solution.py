# The first question
for i in range(45,210):
    if i == 100 :
        continue
    elif i == 205 :
        break

    print(i)

# The second question
a = 0
while a != 168 :
    i = int(input("what is the product of 7 * 24"))
    print(i)
    if i==168:
        print("You answered this Question correctly")
        a = int(i)
    else:
        print("Your Answer is wrong try again..")