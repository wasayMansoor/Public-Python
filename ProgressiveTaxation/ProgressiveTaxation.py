#A Simple Progressive Tax Calculator
#Inputs: IncomeCaps, Tax Rates at each Income Cap, Income
#Coded By Abdulwasay Mansoor

#To DO:
    #Add Exception Handling

#Function That Calculates Total Taxes
def calculateTax(taxRates, incomeCap, income):
    totalTax = 0
    currIncome = income
    for i in range(len(taxRates)):
        if i + 1 == len(taxRates):
            totalTax += currIncome * taxRates[i]
        elif (income>incomeCap[i]):
            totalTax += incomeCap[i] * taxRates[i]
            currIncome = currIncome - incomeCap[i]
        else:
            totalTax += currIncome * taxRates[i]
    return totalTax

#Initializing Tax Percentages And Income Caps List
taxRates = []
incomeCap = []
#Input Of How Many Income Caps there are
numOfCaps = int(input("How Many Income Caps: "))

#Loop For Inputing Individual Caps And Tax Rates At Each Cap
#Then Appending Input To Lists
for i in range(numOfCaps):
    print("Income Cap Number", i+1, "(in thousands): ")
    temp = int(input(">"))
    incomeCap.append(temp*1000)
    print("taxRate Number", i+1, "(as a percentage): ")
    temp = int(input(">"))
    taxRates.append(temp/100)

#Loop Repeated Until User Exits
while True:
    #Input Income With Command For Exiting Program
    income = int(input("Type -1 To Exit Or Type Income(In Thousands): "))
    if income >= 0:
        #Total Tax Calculated By Calling Function
        totalTax = int(calculateTax(taxRates, incomeCap,income))
        #Overall Individual Tax Rate Calculated
        overallTaxRate = totalTax/income

        #Producing And Outputs Dictionary For Easier Output
        outputs = {'TT': totalTax, 'I': income, 'OTR': overallTaxRate}
        print("Total tax of {TT} on an income of {I} with a overall tax rate of {OTR}".format(**outputs))
    #Exit
    elif income == -1:
        exit(0)
    else:
        print("Invalid Input")
