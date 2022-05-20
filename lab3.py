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
while True:
    var=int(input("what is the product of 7 * 24 ?"))
    if var==168:
            print("You answered this Question correctly")
            break
    else:
        print("your answer worng please again..")




