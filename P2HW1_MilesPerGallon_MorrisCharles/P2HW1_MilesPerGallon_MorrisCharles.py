 # this function will caluctae miles per galloin,
 # totoal ags cost and cost per mile.
 # 9/30/21
 # CTI-110 P2HW1 - Miles Per Gallon
 # Charles Morris

 # milesdriven = *user input
 # gallonsused = *user input
 # costpergallon = *user input
 # calucate miles per gallon (milesdriven/gallonsused)
 # calcualte total gas cost (costpergallon*gallonsused)
 # calcuate cost per mile (milesdriven/ totoal gas cost)

milesDriven = float(input('Enter miles driven: '))
gallonsUsed = float(input('Enter gallons used: '))
costPerGallon = float(input('Enter cost per gallon: '))

mpg = (milesDriven/gallonsUsed)
totalGasUsed = (costPerGallon*gallonsUsed)
costPerMile = (totalGasUsed/milesDriven)

print('Miles Per Gallon: ', '{:.2f}'.format(mpg))
print('Total Gas Cost: ', '${:.2f}'.format(totalGasUsed))
print('Cost Per Mile: ', '${:.2f}'.format(costPerMile))
