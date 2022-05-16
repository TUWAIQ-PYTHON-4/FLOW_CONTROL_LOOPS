#First Assignment
for i in range(45,210):
    # print(i)
    if i == 100:
        continue
    else:
        if i == 205:
            break
        print(i)
    

#Second Assignment 
answer = 0
while (answer !=  168):
    answer = int (input("Enter Multiply 7 * 24? "))
    if answer == 168:
        print('Correct answer')
        continue
    else:
        print('your answer is wrong Try Again ')
