# 1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
for number in range (45,210):
    if number == 100:
        continue
    elif number ==205:
        break
    print(number)

# 2) Using a while loop and input , do the following :
while True:
    the_result = input("what is the product of 7 * 24 ?")
    if the_result == "168":
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again")    