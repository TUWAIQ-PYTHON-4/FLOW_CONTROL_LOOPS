from multiprocessing.connection import answer_challenge


for number in range(45 , 210):
    if number == 206:
        break
    elif number == 100:
        continue
    print(number)

answer = 0

while answer != 168:
    answer = int(input("what is the product of 7 * 24 ? : "))
    if answer==168:
        continue
    print("Your Answer is wrong try again..")

print("You answered this Question correctly")
