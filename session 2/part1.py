

# México Tlaxcala Government Manager App
howManyEnterprises = int(input("How many enterprises would you take place this process: "))

for i in range(howManyEnterprises):
    percent = 0
    tenPercent = .10
    twelvePercent = .12
    fourteenPercent = .14
    sixteenPercent = .16
    eighteenPercent = .18  
    twentyPercent = .20
    twentyTwoPercent = .22
    idEnterprise = int(input("Supply your Enterprise id : "))
    nameEnterprise = input("Supply your Enterprise name : ")
    monthRequired = input("Provide please the month over the calculates will be done: ")
    employeesNumber = int(input("Supply your Enterprise employees number: "))
    monthFacturedAmount = int(input("Provide the  month amount over which one calculates will be done: "))
    calculatesManager = 0
      
    if employeesNumber < 11:
        if monthFacturedAmount < 1000:
            percent = tenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
            percent = twelvePercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
            percent = fourteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 500001:
            percent = sixteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        
            
    elif employeesNumber > 10 and employeesNumber < 31:
        if monthFacturedAmount < 1000:
            percent = twelvePercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
            percent = fourteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
            percent = sixteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 500001:
            percent = eighteenPercent
            calculatesManager = (monthFacturedAmount * percent)
            
    elif employeesNumber > 30 and employeesNumber < 51:
        if monthFacturedAmount < 1000:
            percent = fourteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
            percent = sixteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
            percent = eighteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 500001:
            percent = twentyPercent
            calculatesManager = (monthFacturedAmount * percent)
    else:
        if monthFacturedAmount < 1000:
            percent = sixteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
            percent = eighteenPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
            percent = twentyPercent
            calculatesManager = (monthFacturedAmount * percent)
        elif monthFacturedAmount > 500001:
            percent = twentyTwoPercent
            calculatesManager = (monthFacturedAmount * percent)
    result = float(calculatesManager)
    print(f'The { monthRequired } Month Bill Amount to have being paid for { nameEnterprise } with id: { idEnterprise } according the payroll tax corresponding over { percent }%, is: ${ result }')
