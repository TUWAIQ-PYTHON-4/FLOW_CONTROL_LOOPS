'''
 1) Using range(),  make a range from 45 to 210,
  using a for loop iterate over the sequence and print the elements.
   Skip the number 100 and break the loop at 205
'''
for i in range(45, 210):
    if i == 100: continue
    elif i == 205: break
    print(i)

'''
2) Using a while loop and input , do the following :
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

'''

while True:
    answer = input("what is the product of 7 * 24 ?")
    if int(answer) == 168:
        print("You answered this Question correctly")
        break
    print('Your Answer is wrong try again..')




