#Using range(),  make a range from 45 to 210

x = range(45, 210)
for n in x:
    if n == 100:
        continue
     
    elif n == 205:
        break
    print(n)
    break

# ## 2) 
a = int(input("what is the product of 7 * 24 ?"))

if a == 168:
    print("You answered this Question correctly")
else:
    print("Your Answer is wrong try again..")




