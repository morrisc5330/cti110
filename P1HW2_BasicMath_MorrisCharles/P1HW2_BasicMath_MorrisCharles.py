# This will do basic math, it will ask for the monthly price of an item and calcualte how much the user spends with tax monthly and anually
# 9/22/21
# CTI-110 P1HW2 - Basic Math
# Charles Morris

#ask for bill name, ask for money per mounth, find tax, add tax to cost,
#tell amount per year including tax


expName = input('Enter name of expence: ')
expCost = float(input('Enter monthly charge: '))
taxCost = expcost*.06    #find tax of item
taxWCost = taxcost+expcost #finds the cost with tax added

print('Bill: ',expName,'     Before Tax: $',expCost)
print('Monthly Tax: $', taxCost)
print('Monthly Charge: $', taxWCost)
print('Annual Charge: $', taxWCost*12)

