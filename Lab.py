  #make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

for number in range(45,210):
    if number == 100:
       continue
    elif number == 205:
        break
    print(number)
# Ask the the user : "what is the product of 7 * 24 ?"
result = input("what is the product of 7 * 24 ?")

''' check if the answer is right then exit the loop and print "You answered this Question correctly"
 if the answer is wrong, then print "Your Answer is wrong try again.." 
 and show the user the question again.
'''
while result!= '168':
   result= input("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")