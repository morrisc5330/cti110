# This will ask for a number, tell it back to you, square it, then cube it,
# then ask for another number and add and multiply them together
# 9/28/21
# CTI-110 P1HW1_Warm up
# Charles Morris

# Psudo code
# ask for number, tell user number, square it, then cube it, then as for another
# number and then add and multply those two numbers together

userNum = int(input('Enter integer:'))

print('You entered:',userNum)

print(userNum, 'squared is', userNum*userNum) 

print('And', userNum, 'cubed is', userNum*userNum*userNum, '!!')

userNum2 = int(input('Enter another integer:\n'))

print(userNum, '+',userNum2, 'is', userNum2+userNum)

print(userNum, '*',userNum2, 'is', userNum2*userNum)
