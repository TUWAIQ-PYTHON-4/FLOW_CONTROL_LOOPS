'''
1) 
Using range(), 
make a range from 45 to 210, 
using a for loop iterate over the sequence and print the elements. 
Skip the number 100 and break the loop at 205
'''
for i in range(45 , 210):
    if i == 100:
        continue
    elif i == 205:
        break
    print("The number is :" , i)

'''
2)
 Using a while loop and input , do the following :
'''
print("*****************next question********************")


while True:
    user_input = input("what is the product of 7 * 24 ?")

    if int(user_input )== 168:
        print("You answered this Question correctly")
        break
    else:
       print("Your Answer is wrong try again.." )
    continue
        
