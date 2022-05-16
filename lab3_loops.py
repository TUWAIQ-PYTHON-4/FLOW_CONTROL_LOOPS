# FLOW_CONTROL_LOOPS
# 1) 
for number in range(45, 210):
    if number==100:
        continue
    elif number == 205:
        break
    print(number)

# 2)
while True:
    user_result:int = int(input('what is the product of 7 * 24 ?'))
    if user_result == 168:
        print('You answered this Question correctly')
        break
    else:
        print('Your Answer is wrong try again..')
        