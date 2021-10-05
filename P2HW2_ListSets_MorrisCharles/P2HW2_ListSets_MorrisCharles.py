 # this function will ask the user for 6 numbers and show the lowest, highest
 # total, and average number then convert to a set
 # 9/30/21
 # CTI-110 P2HW2 - List Sets
 # Charles Morris

 # listof6 list
 # ask user for 6 number
 # show list
 # identify smallest number
 # identyf the largest
 # calcuate the sum
 # Average the numbers
 # create Set

num1 = float(input('Enter num 1: '))
num2 = float(input('Enter num 2: '))
num3 = float(input('Enter num 3: '))
num4 = float(input('Enter num 4: '))
num5 = float(input('Enter num 5: '))
num6 = float(input('Enter num 6: '))
print()

userList = [num1, num2, num3, num4, num5, num6]

print('Created list')
print(userList)
print('Smallest number in List: ',min(userList))
print('Largest number in List: ',max(userList))
print('Sum of numbers in List: ',sum(userList))
print('Average of numbers in List: ',(sum(userList))/(len(userList)))
print()

setUserList=set(userList)
print('Created set')
print(setUserList)


